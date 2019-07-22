from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from chore_chart.models import Chore, UserProfileInfo
from .forms import UserForm, UserProfileInfoForm, ChoreForm
import json


def index(request):
    profile_images = UserProfileInfo.objects.all()
    context = {'profiles':profile_images}
    return render(request, 'chore_chart/index.html', context=context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def chore_index(request):
    current_user = request.user
    print(current_user.id)
    username = request.user.username
    chores = Chore.objects.all()

    if request.method == 'POST':
        chore = chores.get(id=request.POST.get('chore'))
        userProfileInfo = UserProfileInfo.objects.get(user=current_user.id)
        userProfileInfo.bank += chore.value
        userProfileInfo.save()
        return render(request, 'chore_chart/success.html',{'bank':userProfileInfo.bank})  

    else:
        return render(request, 'chore_chart/chore_index.html', {'username':username, 'chores':chores})

# could use this later.... 


def add_chore_form(request):
    form = ChoreForm()

    if request.method == 'POST':
        form = ChoreForm(request.POST)

        if form.is_valid():
            value = form.cleaned_data['value']
            print("Validation Success!")
            print('Name: ' + form.cleaned_data['chore_name'])
            print('Description: ' + form.cleaned_data['description'])
            print('Value: ' + str(value))
            print('Image: ' + form.cleaned_data['image'])

        else:
            print('not valid')
    else:
        return render(request,'chore_chart/add_chore.html',{})

    return render(request, 'chore_chart/add_chore.html', {'form': form})


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.bank = 0
            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else: 
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,'chore_chart/registration.html',
                            { 
                                'profile_form':profile_form,
                                'user_form':user_form,  
                                'registered':registered,
                            })

def user_login(request):
    username = request.GET.get('username', '')
    error = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                chores = Chore.objects.all()
                response = redirect('/chore-chart/chore-index')
                return response

            else:
                return HttpResponse('Nope')

        else:
            error = True
            return render(request,'chore_chart/user_login.html',{'username':username, 'error':error})

    else:
        return render(request,'chore_chart/user_login.html',{'username':username, 'error':error})

def success(request):

    return render(request, 'chore_chart/success.html',{})


@login_required
def goals(request):
    user = request.user
    userProfileInfo = UserProfileInfo.objects.get(user=user.id)
    bank = userProfileInfo.bank
    goal = userProfileInfo.goal
    if bank and goal is not 0:
        percent = (goal - bank) / goal
        progress = percent * 100
    else:
        progress = 0
    return render(request, 'chore_chart/goals.html', {'goal': goal, 'bank': bank, 'progress':progress})






