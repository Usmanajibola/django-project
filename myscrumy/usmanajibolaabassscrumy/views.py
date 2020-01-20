from django.shortcuts import render
from django.http import HttpResponse
from usmanajibolaabassscrumy.models import GoalStatus, ScrumyGoals, ScrumyHistory

# Create your views here.
goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
def get_grading_parameters(request):
    return HttpResponse(goal)
