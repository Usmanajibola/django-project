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
    dictionary = {'error': 'A record with that goal id does not exist'}
    try:
        goalname = ScrumyGoals.objects.get(goal_id = '%s' % goal_id)
    except Exception as e:
        return render(request, 'usmanajibolaabassscrumy/exception.html', dictionary)
    else:
        return Httpresponse(goalname.goal_id)



def add_goal(request):
    weeklygoal = GoalStatus.objects.get(status_name="Weekly Goal")

    myuser = User.objects.get(username="louis")
    track = list(range(1000, 9999))
    random_number = random.sample(track, k=1)

    for i in random_number:
        value = i

    mygoals = ScrumyGoals(goal_name = 'Keep Learning Django', goal_id = value, created_by='Louis', moved_by='Louis', owner='Louis', goal_status = weeklygoal, user = myuser)
    mygoals.save()

    return Httpresponse(mygoals)

def home(request):
    #goal = ScrumyGoals.objects.get(goal_name = 'Learn Django')
    #return HttpResponse(goal)
    #dictionary = {'goal_name':goal.goal_name, 'goal_id':goal.goal_id, 'user':goal.user}
    all_users = User.objects.all()
    weeklygoal = GoalStatus.objects.get(status_name= "Weekly Goal")
    goalweekly = weeklygoal.scrumygoals_set.all()
    dailygoal = GoalStatus.objects.get(status_name= "Daily Goal")
    goaldaily = dailygoal.scrumygoals_set.all()
    verifygoal = GoalStatus.objects.get(status_name= "Verify Goal")
    goalverify = verifygoal.scrumygoals_set.all()
    donegoal = GoalStatus.objects.get(status_name= "Done Goal")
    goaldone = donegoal.scrumygoals_set.all()

    dictionary = {'user':all_users, 'weekly':goalweekly, 'daily':goaldaily, 'verify':goalverify, 'done':donegoal}
    return render(request, 'usmanajibolaabassscrumy/home.html', dictionary)
