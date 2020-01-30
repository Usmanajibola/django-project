from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usmanajibolaabassscrumy.models import GoalStatus, ScrumyGoals, ScrumyHistory, SignupForm, CreateGoalForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
import random

#Create your views here.
@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
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



def sign_up(request):
    #dictionary = {'error':'invalid login credentials'}
    #return render(request, 'registration/signup.html', dictionary)
    form = SignupForm()
    if request.method == 'POST':
        if form.is_valid():
            form = SignupForm(request.POST)
            form_data = request.POST.dict()

            user  = User.objects.create_user(
            form_data['username'], form_data['email'], form_data['password']
            )
            user.save()
            new_user = User.objects.get(username=form_data['username'])

            group = Group.objects.get(name='Developer')
            group.user_set.add(new_user)
            #success_dic = {'success':'Congrats! SignUp successful'}
            return HttpResponseRedirect('usmanajibolaabassscrumy/signup.html')



    else:
        form
    return render(request, 'registration/signup.html', {'form':form})



@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
def get_grading_parameters(request):
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)

def move_goal(request, goal_id):
    dictionary = {'error': 'A record with that goal id does not exist'}
    try:
        goalname = ScrumyGoals.objects.get(goal_id = '%s' % goal_id)
    except Exception as e:
        return render(request, 'usmanajibolaabassscrumy/exception.html', dictionary)
    else:
        return Httpresponse(goalname.goal_id)

@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
def add_goal(request):

    if request.method == 'POST':
        track = list(range(1000, 9999))
        random_number = random.sample(track, k=1)
        weeklygoal = GoalStatus.objects.get(status_name="Weekly Goal")
        for i in random_number:
            value = i




        if form.is_valid():
            form = CreateGoalForm(request.POST)
            form_data = request.post.dict()

            user = User.objects.get(id=form_data['user'])
            form.save(commit=False)
            form.goal_id = value
            form.created_by = user.username
            form.moved_by = user.username
            form.owner = user.username
            form.goal_status = weeklygoal
            form.save()
            return HttpresponseRedirect('usmanajibolaabassscrumy/home')

    form = CreateGoalForm()

    context = {
    'creategoal':form
    }


    return render(request, 'usmanajibolaabassscrumy/add.html', context)


        #goal = form_data['goal_name']
        #form_user = form_data['username']



        #myuser = User.objects.get(username=form_user)



        #mygoals = ScrumyGoals(goal_name = goal, goal_id = value, created_by='Louis', moved_by='Louis', owner='Louis', goal_status = weeklygoal, user = myuser)
        #mygoals.save()


        #return HttpResponse(mygoals)
