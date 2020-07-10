from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from ChristKart.models import Registration
from ChristKart.forms import UserForm,UserProfileForm
# Create your views here.


class index(TemplateView):
    template_name = 'index.html';
class plates(TemplateView):
    template_name = 'plates.html'

class bags(TemplateView):
    template_name = 'bags.html'
class straws(TemplateView):
    template_name = 'straws.html'



def registerView(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'register_form.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



########################################



def user_login(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('ChristKart:home'))
            else:
                return HttpResponse('Account not active')

        else:
            return HttpResponse("Invalid Login Credentials")
    else:
        return render(request,'user_login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ChristKart:home'))
