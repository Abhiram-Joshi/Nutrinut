from django.shortcuts import render
from app.models import UserProfile, FoodCalories
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from app.forms import UserProfileForm, UserNamePassForm, DayMealForm, BFoodForm, LFoodForm, DFoodForm,\
                                                                      RBFoodForm, RLFoodForm, RDFoodForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active!!")

        else:
            return HttpResponse("User not found!")

    else:
        return render(request, 'login.html')



def signup(request):
    registered = False

    if request.method=='POST':
        user_profile_form = UserProfileForm(request.POST)
        user_namepass_form = UserNamePassForm(request.POST)

        if user_profile_form.is_valid() and user_namepass_form.is_valid():


            user = user_namepass_form.save()
            user.set_password(user.password)
            user.save()

            obj = UserProfile()
            obj.birthdate = user_profile_form.cleaned_data['birthdate']
            obj.weight = user_profile_form.cleaned_data['weight']
            obj.height = user_profile_form.cleaned_data['height']
            obj.user = user
            obj.save()




            registered = True

        else:
            print(user_profile_form.errors)


    else:
        user_profile_form = UserProfileForm()
        user_namepass_form = UserNamePassForm()

    context_dict = {
        'registered':registered,
        'user_profile_form':user_profile_form,
        'user_namepass_form':user_namepass_form
    }

    return render(request, 'signup.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def menu(request):

    if request.method == "POST":
        daymealform = DayMealForm(request.POST)

        if daymealform.is_valid():
            day = daymealform.cleaned_data['day']
            meal = daymealform.cleaned_data['meal']

            return render(request, 'mess.html', {'day':day})


    else:
        return render(request, 'menu.html', {'daymealform':DayMealForm})


def mess(request):
    return HttpResponse("Mess")


@login_required
def breakfast(request):

    if request.method == "POST":

        foodform = BFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))



            for i in selected_items:
                request.user.profile.calories += all_food_items[i]

            request.user.profile.save()

            return HttpResponseRedirect(reverse('lunch'))



    return render(request, 'breakfast.html', {'BFoodForm':BFoodForm})


@login_required
def lunch(request):

    if request.method == "POST":

        foodform = LFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))



            for i in selected_items:
                request.user.profile.calories += all_food_items[i]

            request.user.profile.save()

            return HttpResponseRedirect(reverse('dinner'))


    return render(request, 'lunch.html', {'LFoodForm':LFoodForm})


@login_required
def dinner(request):

    if request.method == "POST":

        foodform = DFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))



            for i in selected_items:
                request.user.profile.calories += all_food_items[i]

            request.user.profile.save()

            cals = request.user.profile.calories

            request.user.profile.calories = 0
            request.user.profile.save()

            per = cals/2500*100

            return render(request, 'final.html', {'calories':cals, 'll':2300, 'ul':2700, 'per':per, 'ideal_cal':2500})


    return render(request, 'dinner.html', {'DFoodForm':DFoodForm})

@login_required
def restaurant(request):
    return render(request, 'restaurant.html')

@login_required
def rbreakfast(request):

    if request.method == "POST":

        foodform = RBFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))


            cals = 0
            for i in selected_items:
                cals += all_food_items[i]

            per = cals/350*100
            print(per)
            return render(request, 'final.html', {'calories':cals, 'll':300, 'ul':400,'per':per, 'ideal_cal':350})


    return render(request, 'rbreakfast.html', {'RBFoodForm':RBFoodForm})

@login_required
def rlunch(request):

    if request.method == "POST":

        foodform = RLFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))


            cals = 0
            for i in selected_items:
                cals += all_food_items[i]

            per = cals/600*100

            return render(request, 'final.html', {'calories':cals, 'll':500, 'ul':700, 'per':per, 'ideal_cal':600})


    return render(request, 'rlunch.html', {'RLFoodForm':RLFoodForm})

@login_required
def rdinner(request):

    if request.method == "POST":

        foodform = RDFoodForm(request.POST)


        if foodform.is_valid():

            selected_items = request.POST.getlist('food')

            all_food_items = dict(FoodCalories.objects.values_list('name','calories'))


            cals = 0
            for i in selected_items:
                cals += all_food_items[i]

            per = cals/600*100

            return render(request, 'final.html', {'calories':cals, 'll':500, 'ul':700, 'per':per, 'ideal_cal':600})


    return render(request, 'rdinner.html', {'RDFoodForm':RDFoodForm})
