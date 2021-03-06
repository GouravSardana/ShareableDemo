from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate


class Home(TemplateView):
    template_name = 'home.html'


class Login(TemplateView):
    template_name = 'login.html'


class Signup(TemplateView):
    template_name = 'signup.html'


class Investor(TemplateView):
    template_name = 'investor.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            first_name = self.request.POST.get('first_name')
            email = self.request.POST.get('email')
            username = self.request.POST.get('username')
            password = self.request.POST.get('password')
            form = User.objects.create_user(first_name=first_name, email=email, username=username,
                                            password=password)
            group = Group.objects.get(name='Investor')
            form.groups.add(group)
            form.save()
            return HttpResponseRedirect(reverse('user_login'))

class Borrower(TemplateView):
    template_name = 'borrower.html'
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            first_name = self.request.POST.get('first_name')
            email = self.request.POST.get('email')
            username = self.request.POST.get('username')
            password = self.request.POST.get('password')
            form = User.objects.create_user(first_name=first_name, email=email, username=username,
                                            password=password)
            group = Group.objects.get(name='Borrower')
            form.groups.add(group)
            form.save()
            return HttpResponseRedirect(reverse('user_login'))


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')


        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)

                if user.groups.filter(name='Investor'):
                    return HttpResponse('Hey Investor')
                elif user.groups.filter(name='Borrower'):
                    return HttpResponse('Hey Borrower')
                else:
                    return HttpResponse('Not Borrower Not Customer')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))


class About(TemplateView):
    template_name = 'about.html'


class Community(TemplateView):
    template_name = 'community.html'