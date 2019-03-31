from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect

from topic.models import Topic, TopicInstance, Team
from .forms import UserForm, SolveProblemForm, TeamForm
# Create your views here.
from django.views.generic import DetailView, UpdateView, CreateView
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
        self.request.user.team = self.object
        self.request.user.is_master = True
        self.request.user.save()
        return HttpResponseRedirect(reverse_lazy('team_detail', kwargs={'pk': self.object.id}))


class TeamDetailView(DetailView):
    template_name = "accounts/team_detail.html"
    model = Team
