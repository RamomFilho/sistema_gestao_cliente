from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


def home(request):
    value1 = 10
    value2 = 20
    res = value1 * value2
    return render(request, 'home/home.html', {'result': res})


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá, seja bem minha a minha página, Ramom!'
        return context


class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
