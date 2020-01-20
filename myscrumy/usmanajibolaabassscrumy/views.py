from django.shortcuts import render
from django.http import HttpResponse
from usmanajibolaabassscrumy.models import GoalStatus, ScrumyGoals, ScrumyHistory
from django.contrib.auth.models import User
import random

#Create your views here.
goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
def get_grading_parameters(request):
    return HttpResponse(goal)

def move_goal(request, goal_id):
    goalname = ScrumyGoals.objects.get(goal_id = '%s' % goal_id)
    return HttpResponse(goalname.goal_name)

def add_goal(request):
    weeklygoal = GoalStatus.objects.get(status_name="Weekly Goal")
    new_user = User.objects.create(username='Louis Oma')

    myuser = User.objects.get(username="Louis Oma")
    track = list(range(1000, 10000))
    random_number = random.sample(track, k=1)

    for i in random_number:
        value = i

    mygoals = ScrumyGoals(goal_name = 'Keep Learning Django', goal_id = value, created_by='Louis', moved_by='Louis', owner='Louis', goal_status = weeklygoal, user = myuser)
    mygoals.save()

def home(request):
    goal = ScrumyGoals.objects.filter(goal_name = 'Keep Learning Django')
    return HttpResponse(goal)
