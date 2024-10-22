from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django_filters import rest_framework
from rest_framework import filters
from rest_framework import generics
from .models import Sotrudniki, Dolznosti
from .serializers import HoseSerializers
from .forms import AuthForm


def glavnpage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    mas = Sotrudniki.objects.using('default').all()
    mas1 = Dolznosti.objects.using('default').all()
    if request.method == 'POST':
        if 'Сохранить изменения' in request.POST:
            uda = Sotrudniki.objects.using('default').filter(id=int(request.POST.get('Сохранить изменения', ''))).\
                values_list('uda')
            a = Sotrudniki.objects.using('default').get(id=int(request.POST.get('Сохранить изменения', '')))
            if request.POST.get('izm1', '') != '':
                a.fio = request.POST.get('izm1', '')
            a.dol_id = request.POST.get('izm2', '')
            if request.POST.get('izm3', '') != str(uda[0])[1]:
                a.uda = request.POST.get('izm3', '')
                if request.POST.get('izm3', '') == '1':
                    a.dat = datetime.now().strftime('%d.%m.%Y')
            if request.POST.get('izm4', '') != '':
                a.dat = request.POST.get('izm4', '')
            a.save()
        elif 'Удалить' in request.POST:
            a = Sotrudniki.objects.using('default').filter(id=int(request.POST.get('Удалить', '')))
            a.delete()
        elif 'Зарегистрировать' in request.POST:
            if (request.POST.get('rega1', '') != '') and (request.POST.get('rega2', '') != ' '):
                dol = Dolznosti.objects.using('default').filter(dol=request.POST.get('rega2', '')).values_list('id')
                a = Sotrudniki.objects.using('default').create(fio=request.POST.get('rega1', ''),
                                                               dol_id=int(str(dol[0])[1]),
                                                               uda='0', dat=datetime.now().strftime('%d.%m.%Y'))
    context = {
        'title': 'Главная', 'mas': mas, 'mas1': mas1,
    }
    return render(request, 'hose/glavn.html', context)


def loginpage(request):
    title = 'Вход'
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    auth_form.add_error('__all__', 'Ошибка. Учетная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка. Проверьте правильно ли вы написали логин и пароль')
    else:
        auth_form = AuthForm()
    context = {'title': title, 'form': auth_form}
    return render(request, 'hose/login.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')


class HoseAPIView(generics.ListAPIView):
    queryset = Sotrudniki.objects.all()
    serializer_class = HoseSerializers
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['uda']
