from functools import wraps
from apps.user.models import UserInfo
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html')

# Create your views here.
class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        matrix = request.POST.get('matrix')
        email = request.POST.get('matrix')
        error = {
            'error': 'User is Exist ! Please Sign In',
        }
        if 12 >= len(username) >= 6:
            if password1 == password2 and 26 >= len(password1) >= 6:
                if UserInfo.objects.filter(username=username).first():
                    return render(request, '404.html', context=error)
                if matrix == 'administor':
                    user = UserInfo(username=username, password=make_password(password=password1), email=email,
                                    is_staff=True)
                else:
                    user = UserInfo(username=username, password=make_password(password=password1), email=email)
                user.save()
                # 设置session
                request.session["is_login"] = "1"
                request.session["name"] = username
                return redirect("/", content={'username': username})
            else:
                error['error'] = 'Username or Password Error , Please Check Up !  '
                return render(request, '404.html', context=error)
        error['error'] = 'Username so Short !'
        return render(request, '404.html', context=error)
