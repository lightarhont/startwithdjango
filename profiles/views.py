from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profiles

varshow = 'profiles/show.html'
varedit = 'profiles/edit.html'

def r(request, data, header, tpl=varshow, vtype='show', msgtype='none', msg=''):
    params = {}
    params['header'] = header
    params['data'] = data
    params['type'] = vtype
    params['msgtype'] = msgtype
    params['home'] = request.get_host()
    if msg != '':
        params['msg'] = msg    
    if request.user.is_authenticated():
        params['auth'] = True
    
    return render_to_response(tpl, params)

def getdata(userid):
    return Profiles.objects.filter(userid=userid)[0]

def show(request):
    title = 'Просмотр профиля'
    if request.method == 'POST':
        if request.POST.get('logout') == '1':
            logout(request)
            return redirect('show.html')
        else:
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('show.html')
                else:
                    msg = 'При авторизации возникли ошибки. Учётная запись неактивна!'
            else:
                msg = 'При авторизации возникли ошибки. Возможно неправильный логин или пароль!'
    
        return r(request, getdata(1), msg, msgtype='alert', msg=msg)
    else:
        return r(request, getdata(1), title)


def edit(request):
    
    if request.method == 'POST':
        item = getdata(request.user.id)
        item.userid = int(request.POST.get('userid'))
        item.fname = request.POST.get('fname')
        item.lname = request.POST.get('lname')
        item.bdate = int(request.POST.get('bdate'))
        item.biography = request.POST.get('biography')
        item.contacts = request.POST.get('contacts')
        item.save()
        msg = 'Редактирование профиля. Данные сохранены!'
        return r(request, getdata(request.user.id), msg, tpl=varedit, vtype='edit', msgtype='success', msg=msg)
    else:    
        title = 'Редактирование профиля'
        if not request.user.is_authenticated():
            return redirect('show.html')
        else:
            return r(request, getdata(request.user.id), title, tpl=varedit, vtype='edit')
    