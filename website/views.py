"""Import line."""
from unicodedata import name
from user.models import *
from website.models import NFT, Trade
from website.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
import time


class DataMixin:
    """Class line."""

    def __init__(self):
        """Function line."""
        self.context = 0

    def get_user_context(self, **kwargs):
        """Function line."""
        self.context = kwargs
        if 'cat_selected' not in self.context:
            self.context['cat_selected'] = 0
        return self.context


class RegUser(DataMixin, CreateView):
    """Class line."""
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """Function line."""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Reg')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    """Class line."""
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        """Function line."""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign_in')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    """Function line."""
    logout(request)
    return redirect('/')

# Create your views here.


def main_page(request):
    """Function line."""
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
            description=description,
            owner = request.user,
            in_market= 'false')
        print(request.user) 
        nft.save()
        return redirect('/market/')
    return render(request, 'main.html', context)


def login_page(request):
    """Function line."""
    context = {'page': 'create'}
    return render(request, 'login.html', context)

@login_required
def data_post_id(request, post_id):
    """Function line."""
    query = get_object_or_404(NFT, id=post_id)
    context = {'form': query}
    return render(request, 'one_nft.html', context)

@login_required
def profile_page(request):
    """Function line."""
    person = get_object_or_404(CustomUser, username=request.user)
    if request.method == 'POST':
        profile_image = request.FILES.get('myfile')
        print('in post')
        person.profile_pic = profile_image
        print(profile_image)
        person.save()
    context = {'page': 'profile', 'height': '20', 'form': person}
    return render(request, 'profile.html', context)

@login_required
def game_page(request):
    """Function line."""
    context = {'height': '40', 'page': 'game'}
    return render(request, 'game.html', context)

@login_required
def inventory_page(request):
    """Function line."""

    context = {
        'all_data': NFT.objects.filter(owner=str(request.user), in_market='false'),
        'page': 'inventory',
        'height': '40'
    }
    if request.method == 'GET':

        try:
            sort = request.GET['sort']
        except BaseException:
            sort = ''

        if sort == 'name':
            context = {
                'all_data': NFT.objects.filter(
                    owner=str(
                        request.user)).order_by('name'),
                'page': 'inventory',
                'height': '40'}
        if sort == 'price':
            context = {'all_data': NFT.objects.filter(owner=str(request.user)).order_by(
                '-price')[::-1], 'page': 'inventory', 'height': '40'}
    return render(request, 'inventory.html', context)


@login_required
def clicker_page(request):
    """Function line."""

    if request.method == 'POST':
        player = get_object_or_404(CustomUser, username=request.user)
        player.balance += min(100000, abs(int((request.POST.get('balance')))))
        player.save()
    context = {'page': 'clicker'}
    return render(request, 'clicker.html', context)


@login_required
def market_page(request):
    """Function line."""
    context = {
        'all_data': NFT.objects.filter(in_market= 'true'),
        #.exclude(owner=str(request.user))
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
                'all_data': NFT.objects.order_by('name'),
                'page': 'market',
                'height': '40'
            }
        if sort == 'price':
            context = {
                'all_data': NFT.objects.order_by('-price')[::-1],
                'page': 'market',
                'height': '40'
            }
    return render(request, 'market.html', context)
@login_required
def trade_page(request):
    context = {}
    if request.method == 'POST':
        try:
            make = request.POST.get('make')
        except: pass
    print(make)
    if int(make):
        trade_time = time.time()
        query = get_object_or_404(NFT, id=make)
        trade = Trade(id_nft=query.id, price_array  = query.price)
        print(int(0.7*query.price),int(1.3*query.price))
        context.update({
         'page' :  'trades',
        'nft_price_l' : int(0.7*query.price),
        'nft_price_h' : int(1.3*query.price),
        'nft_price' : int(query.price),
        'nft_name' : str(query.name),
        'time' : str(trade_time),
        })
        return render(request, 'make_trade.html', context)


@login_required
def my_trades_page(request):
    context = {
        'all_data': Trade.objects.filter(new_owner = str(request.user)) ,
        'page' :  'trades',
        'height': '40'
    }
    return render(request, 'my_trades.html', context)


@login_required
def transaction(request):
    """Function line."""
    context = {}
    if request.method == 'POST':
        if 1:
            sec = time.time()
            struct = time.localtime(sec)
            trade_time = time.strftime('%d.%m.%Y %H:%M', struct)
            make = request.POST.get('name')
            print(make)
            query = get_object_or_404(NFT, name=str(make))
            print(1)
            text = request.POST.get('message')
            print(2)
            trade_price = request.POST.get('trade_price')
            print(3)
            print(query.owner)
            trade = Trade(id_nft=query.id, price_array=trade_price, chat=text, owner = str(query.owner), new_owner=str(request.user), time= trade_time )
            print(4)
            trade.save()
            print(5)  
            context.update({
                    'text': 'operation compleate!!!!'})  
        #except: 
       #     context.update({
        #            'text': 'Error'})    
        return render(request, 'operation.html', context)



    if request.method == 'GET':
        buy = request.GET.get('buy_id')
        sell = request.GET.get('sell_id')
        print(buy, type(buy))
        print(sell, type(sell))
        person = get_object_or_404(CustomUser, username=request.user)
       # print(person.balance)
        #print(person)
        if sell  :
            ass = get_object_or_404(NFT, id=sell)
            if person.username == str(ass.owner):
                ass.in_market='true'
                print('TRUE')
                ass.save()
                
                context.update({
                    'text': 'operation compleate!!!!'})
            else:
                context.update({
                    'text': 'Not enought money or it is yours :('})    
        elif buy :    
            ass = get_object_or_404(NFT, id=int(buy))
            print(ass)
            if int(
                person.balance) >= int(
                ass.price) and str(
                person.username) != str(
                    ass.owner):
                owner1 = get_object_or_404(CustomUser, username=ass.owner)    
                #print(person.balance)
                #print(person.balance)
                owner1.balance+= int(ass.price)
                owner1.save()
                person.balance -= int(ass.price)
                person.save()
                ass.in_market='false'
                
                print(person.balance)
                ass.owner = str(request.user)
                ass.save()
                context.update({
                    'text': 'operation compleate!!!!'})
            else:
                context.update({
                    'text': 'Not enought money or it is yours :('})
    return render(request, 'transaction.html', context)

@login_required
def create_page(request):
    """Function line."""
    context = {
        'page': 'create'
    }
    return render(request, 'create_NFT.html', context)
