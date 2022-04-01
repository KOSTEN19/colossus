from django.shortcuts import render, redirect
from website.models import NFT
import datetime
from website.forms import *
from random import randint
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import View
from django.urls import reverse
from django.shortcuts import get_object_or_404


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


class Reg_user(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Reg')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign_in')
        return dict(list(context.items()) + list(c_def.items()))


def LogoutUser(request):
    logout(request)
    return redirect('/')

# Create your views here.


def main_page(request):
    context = {'page': 'main'}
    if request.method == 'POST':
        namenft = request.POST.get('name')
        pricenft = request.POST.get('price')
        nftimage = request.FILES.get('myfile')
        description = request.POST.get('description')
        nft = NFT(
            image=nftimage,
            name=namenft,
            price=pricenft,
            description=description)
        nft.save()
    return render(request, 'main.html', context)


def login_page(request):
    context = {'page': 'create'}
    return render(request, 'login.html', context)


def data_post_id(request, post_id):
    ass = get_object_or_404(NFT, id=post_id)
    q = get_object_or_404(NFT, id=post_id)
    context = {'form': q}
    return render(request, 'one_nft.html', context)


def profile_page(request):
    context = {'page': 'profile', 'height': '20'}
    return render(request, 'profile.html', context)


def game_page(request):
    context = {'height': '40', 'page': 'game'}
    return render(request, 'game.html', context)


def inventory_page(request):
    #ass= list(get_object_or_404(NFT,owner=str(request.user)))
    ass = NFT.objects.filter(owner=str(request.user))
    context = {'all_data': ass, 'height': '40'}
    return render(request, 'market.html', context)


def clicker_page(request):
    context = {'page': 'clicker'}
    return render(request, 'clicker.html', context)


def market_page(request):
    contex = {}
    context = {
        'all_data': NFT.objects.all(),
        'page': 'market',
        'height': '40'
    }
    if request.method == 'GET':

        try:
            sort = request.GET['sort']
        except BaseException:
            sort = ''

        if sort == 'name':
            context = {
                'all_data': NFT.objects.order_by('name')[::-1],
                'page': 'market',
                'height': '40'
            }
        if sort == 'name':
            context = {
                'all_data': NFT.objects.order_by('price')[::-1],
                'page': 'market',
                'height': '40'
            }
    return render(request, 'market.html', context)


def transaction(request):
    context = {}
    if request.method == 'GET':
        try:
            sort = request.GET.get('buy_id')
            ass = get_object_or_404(NFT, id=sort)
            ass.owner = str(request.user)
            ass.save()
            context.update({
                'text': 'transaction compleate!!!!'})
        except BaseException:
            sort = ''
            context.update({'text': 'something go bad :('})
    return render(request, 'transaction.html', context)


def create_page(request):
    context = {

        'page': 'create'

    }

    return render(request, 'create_NFT.html', context)


def LogoutUser(request):
    print('logout')
    logout(request)
    return redirect('/')
