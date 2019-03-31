from accounts.models import Member, SolveProblem
from topic.models import Team


def get_score_by_member(member: Member):
    solved_problems = SolveProblem.objects.filter(member=member)
    integral = 0
    for solved_problem in solved_problems:
        integral += solved_problem.integral
    return integral


def get_score_by_team(team: Team):
    integral = 0
    members = Member.objects.filter(team=team)
    for member in members:
        integral += get_score_by_member(member)
    return integral