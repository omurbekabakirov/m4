from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, LoginForm, SMSCodeForm, ConfirmForm
from django.shortcuts import render, redirect
from users.models import Profile,SMSCode
import random


def register_view(request):
    if request.method == "GET":
        return render(request, 'user/register.html', {'form': RegisterForm()})
    elif request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_active=False,
            )
            Profile.objects.create(
                user=user,
                avatar=avatar,
                bio=bio
            )
            code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            SMSCode.objects.create(
                user=user,
                code=code
            )
            return redirect('confirm', code=code)
        else:
            return render(request, 'user/register.html', {"form": form})




def confirm_view(request, code):
    if request.method == 'GET':
        return render(request, 'user/confirm.html', {'form': ConfirmForm(), 'code': code})
    elif request.method == "POST":
        form = ConfirmForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['code']
            if entered_code == code:
                if SMSCode.objects.filter(code=code).exists():
                    sms_code = SMSCode.objects.get(code=code)
                    sms_code.user.is_active = True
                    sms_code.user.save()
                    sms_code.delete()
                    return redirect('login')
                else:
                    form.add_error(None, "Invalid code")
            else:
                form.add_error('code', "Invalid code")
        return render(request, 'user/confirm.html', {'form': form, 'code': code})
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,
                      'user/login.html',
                      {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request,
                          'user/login.html',
                          {'form': form})
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error(None, 'Invalid username or password')
            return render(request, 'user/login.html',
                          {'form': form})
        login(request, user)
        return redirect('main_view')


@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'user/profile.html')


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('main_view')
