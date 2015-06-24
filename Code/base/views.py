from django.shortcuts import render, redirect

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from api.sysu import Sysuer
from api.parser import parseResultOfCourseSelection, parseScore
from api.getInfo import getGrades
import os

# Create your views here.

@login_required
@require_GET
def index(request):
    return render(request, 'base/index.html')

@login_required
def test(request):
    test = Sysuer(username=request.user.username,
        cookie=request.session['cookie'])
    data = parseResultOfCourseSelection(test)
    return render(request, 'base/test.html', {
        'data': data,
        })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated():
        return redirect('/')

    nextPage = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        cookie = request.POST.get('cookie', None)
        captcha = request.POST.get('captcha', None)
        rno = request.POST.get('rno', None)
        image = request.POST.get('image', None)
        if username and password and cookie and captcha and rno:
            sysuer = Sysuer(username=username, password=password, cookie=cookie)
            try:
                sysuer.login(captcha, rno)
                success = True
            except:
                success = False
            if success:
                nextPage = request.POST.get('next', '/')
                saveImageAsCorrectName(image, captcha)
                request.session['cookie'] = cookie
                user, created = User.objects.get_or_create(username=username)
                user.set_password(password)
                user.save()
                if created:
                    getGrades(user, sysuer)
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect(nextPage)
    user = Sysuer()
    user.getLoginData()
    return render(request, 'base/login.html', {
        'cookie': user.cookie,
        'image': user.image,
        'rno': user.rno,
        'next': nextPage,
    })

def saveImageAsCorrectName(path, name):
    os.rename(os.path.join('media', 'captcha', path.split('/')[1]),
        os.path.join('media', 'captcha', str(name) + '.jpg'))

@require_GET
def logout(request):
    auth.logout(request)
    return redirect('/login/')
