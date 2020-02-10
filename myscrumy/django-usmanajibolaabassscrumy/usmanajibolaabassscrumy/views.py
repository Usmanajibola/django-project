from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from usmanajibolaabassscrumy.models import GoalStatus, ScrumyGoals, ScrumyHistory, SignupForm, CreateGoalForm, MoveMyGoalForm
from django.contrib.auth.models import User, Group, auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

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
    displayuser = request.user.get_username()

    dictionary = {'user':all_users, 'weekly':goalweekly, 'daily':goaldaily, 'verify':goalverify, 'done':goaldone, 'displayuser':displayuser}
    return render(request, 'usmanajibolaabassscrumy/home.html', dictionary)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

        else:
            return redirect('login')

    else:
        return redirect ('login')

    return render (request,'login.html')

def sign_up(request):
    #dictionary = {'error':'invalid login credentials'}
    #return render(request, 'registration/signup.html', dictionary)
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user  = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name
            )
            user.save()
            print('signup successful')
            new_user = User.objects.get(username=username)

            group = Group.objects.get(name='Developer')
            group.user_set.add(new_user)
            #success_dic = {'success':'Congrats! SignUp successful'}
            return HttpResponseRedirect('signupsuccess')



    else:
        form
    return render(request, 'registration/signup.html', {'form':form})



@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
def get_grading_parameters(request):
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)


@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
def move_goal(request, goal_id):


    form = MoveMyGoalForm()

    now_user = request.user
    current_group = Group.objects.get(user=now_user)
    if request.method == 'POST':
        form = MoveMyGoalForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data['goal_status']
            username = form.cleaned_data['user']
            status_based = GoalStatus.objects.get(status_name = status)
            current_user = User.objects.get(username = username)
            done_goal = GoalStatus.objects.get(status_name = 'Done Goal')
            weeklygoal = GoalStatus.objects.get(status_name = 'Weekly Goal')

            move_goal = form.save(commit=False)


            if now_user.groups.filter(name = 'Developer').exists() == True:
                if now_user != current_user:
                    return HttpResponse('Youre not permitted to move goals for other users')
                else:
                    if move_goal.goal_status == done_goal:
                        return HttpResponse('You are not allowed to move your goals to done')
                    else:

                        current_goals = ScrumyGoals.objects.get(goal_id = goal_id)

                        current_goals.goal_status = status_based
                        current_goals.user = current_user

                        current_goals.save()

                        return HttpResponseRedirect('home')

            elif now_user.groups.filter(name = 'Quality Assurance').exists() == True:
                if now_user == current_user:
                    current_goals = ScrumyGoals.objects.get(goal_id = goal_id)

                    current_goals.goal_status = status_based
                    current_goals.user = current_user

                    current_goals.save()

                    return HttpResponseRedirect('home')
                else:
                    current_goals = ScrumyGoals.objects.get(goal_id = goal_id)
                    ver_goal = GoalStatus.objects.get(status_name = 'Verify Goal')



                    current_goals.goal_status = status_based
                    current_goals.user = current_user

                    current_goals.save()

                    return HttpResponseRedirect('home')

            elif now_user.groups.filter(name = 'Admin').exists() == True:
                current_goals = ScrumyGoals.objects.filter(user = request.user)[0]

                current_goals = ScrumyGoals.objects.get(goal_id = goal_id)

                current_goals.goal_status = status_based
                current_goals.user = current_user

                current_goals.save()

                return HttpResponseRedirect('home')

            elif now_user.groups.filter(name = 'Owner').exists() == True:
                if now_user != current_user:
                    return HttpResponse('Youre not permitted to move goals for other users')
                else:
                    current_goals = ScrumyGoals.objects.get(goal_id = goal_id)

                    current_goals.goal_status = status_based
                    current_goals.user = current_user

                    current_goals.save()

                    return HttpResponseRedirect('home')
            else:
                return HttpResponse('The group you specified does not exist')





            #tmp_save = form.save(commit=False)


            #tmp_save.moved_by = user.moved_by
            #tmp_save.created_by = user.created_by
            #tmp_save.owner = user.owner
            #tmp_save.goal_name = user.goal_name
            #tmp_save.goal_id = user.goal_id



            #return HttpResponseRedirect('home')


    context = {
    'move':form,
    }

    return render (request, 'usmanajibolaabassscrumy/movegoal.html', context)
    #dictionary = {'error': 'A record with that goal id does not exist'}
    #try:
        #goalname = ScrumyGoals.objects.get(goal_id = '%s' % goal_id)
    #except Exception as e:
        #return render(request, 'usmanajibolaabassscrumy/exception.html', dictionary)
    #else:
        #return HttpResponse(goalname.goal_id)





@login_required(login_url="/usmanajibolaabassscrumy/accounts/login")
def add_goal(request):
    form = CreateGoalForm()

    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        track = list(range(1000, 9999))
        random_number = random.sample(track, k=1)
        weeklygoal = GoalStatus.objects.get(status_name="Weekly Goal")
        for i in random_number:
            value = i

        if form.is_valid():
            username = form.cleaned_data['user']
            goal_name = form.cleaned_data['goal_name']
            user = User.objects.get(username=username)

            add_goal = form.save(commit=False)

            add_goal.goal_id = value
            add_goal.created_by = user.username
            add_goal.moved_by = user.username
            add_goal.owner = user.username
            add_goal.goal_status = weeklygoal
            add_goal.save()
            return HttpResponseRedirect('home')

    context = {
    'creategoal':form
    }


    return render(request, 'usmanajibolaabassscrumy/add.html', context)

def signupsuccess(request):
    return render(request, 'usmanajibolaabassscrumy/signupsuccess.html')


        #goal = form_data['goal_name']
        #form_user = form_data['username']



        #myuser = User.objects.get(username=form_user)



        #mygoals = ScrumyGoals(goal_name = goal, goal_id = value, created_by='Louis', moved_by='Louis', owner='Louis', goal_status = weeklygoal, user = myuser)
        #mygoals.save()


        #return HttpResponse(mygoals)
