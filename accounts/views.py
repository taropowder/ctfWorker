from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect

from accounts.utils import get_score_by_member
from topic.models import Topic, TopicInstance, Team
from .forms import UserForm, SolveProblemForm, TeamForm, JoinTeamForm
# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView, FormView
from django.urls import reverse_lazy

from accounts.models import Member, SolveProblem


class MemberDetailView(DetailView):
    template_name = 'accounts/accounts_detail.html'
    model = Member


class MemberUpdateView(UpdateView):
    template_name = 'accounts/accounts_form.html'
    model = Member
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('account_detail', kwargs=self.kwargs)


class solveProblemView(CreateView):
    model = SolveProblem
    form_class = SolveProblemForm

    def form_valid(self, form):
        result = {}
        self.object = form.save(commit=False)
        topic = TopicInstance.objects.get(id=form.data['topic'])
        if topic.flag == form.data['flag']:
            self.object.member = self.request.user
            result['message'] = "提交正确"
            result['status'] = True
            try:
                self.object.save()
            except IntegrityError:
                result['message'] = "您已经提交过FLAG，请勿重复提交"
                result['status'] = False

        else:
            result['message'] = "FLAG错误"
            result['status'] = False
        return JsonResponse(result)


class TeamCreateView(CreateView):
    template_name = "accounts/team_form.html"
    form_class = TeamForm

    def form_valid(self, form):
        self.object = form.save()
        user = self.request.user
        user.team = self.object
        user.is_leader = True
        user.save()
        return HttpResponseRedirect(reverse_lazy('team_detail', kwargs={'pk': self.object.id}))


class TeamDetailView(DetailView):
    template_name = "accounts/team_detail.html"
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['members'] = Member.objects.filter(team=self.object)
        context['all_score'] = 0
        for member in context['members']:
            context['all_score'] += member.score
        return context


class TeamJoinView(FormView):
    template_name = 'accounts/team_join.html'
    form_class = JoinTeamForm

    def form_valid(self, form):
        team = Team.objects.filter(uuid=form.data['uuid']).filter(name=form.data['name']).first()
        if team:
            user = self.request.user
            user.team = team
            user.save()
            return HttpResponseRedirect(reverse_lazy('team_detail', kwargs={'pk': team.id}))
        else:
            form.add_error(None, "UUID 和 队伍名称不匹配")
            return self.form_invalid(form)
