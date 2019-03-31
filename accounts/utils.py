from accounts.models import Member, SolveProblem


def get_score_by_member(member: Member):
    solved_problems = SolveProblem.objects.filter(member=member)
    integral = 0
    for solved_problem in solved_problems:
        integral += solved_problem.integral
    return integral
