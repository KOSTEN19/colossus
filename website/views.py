"""Import line."""
import time
import numpy as np
from PIL import Image, ImageChops
from website.models import NFT, Trade
from website.forms import CustomUserCreationForm, CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView



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


def calcdiff(im1, im2):
    """Function line."""
    dif = ImageChops.difference(im1, im2)
    return np.mean(np.array(dif))


def main_page(request):
    """Function line."""
    context = {'page': 'main'}
    if request.method == 'POST':
        namenft = request.POST.get('name')
        pricenft = request.POST.get('price')
        nftimage = request.FILES.get('myfile')
        description = request.POST.get('description')
        count = request.POST.get('count')
        print('---')
        try:
            print('---')
            Image.open(nftimage)
            print(Image.open(nftimage).verify())
           
        except:
            return redirect('/create/')
        

        data = NFT.objects.all()
        unique = True
        if len(data)>0:
            for i in data:
                im1 = Image.open(nftimage).convert('RGB')
                im2 = Image.open(i.image).convert('RGB')
                raz = calcdiff(im1,im2)
                if raz < 15:
                    unique = False
                    print(raz, unique)
        if unique:
            for i in  range(abs(int(count))):
                try:
                    nft = NFT(
                        image=nftimage,
                        name=namenft,
                        price=abs(int(pricenft)),
                        description=description,
                        owner = request.user,
                        id_in_arr = i,
                        in_market= 'false',
                        count = int(count))
                    nft.save()
                except:
                    return redirect('/create/')
        if unique:
            return redirect('/inventory/')
        else:
            messages.error(request,'NFT is not unique!!!')
            print('here')
            return redirect('/create/')
    print('BAN')
    return render(request, 'main.html', context)


def login_page(request):
    """Function line."""
    context = {'page': 'create'}
    return render(request, 'login.html', context)

@login_required
def data_post_id(request, post_id):
    """Function line."""
    query = get_object_or_404(NFT, id=post_id)
    context = {'form': query,
     'all_data': Trade.objects.filter(id_nft=post_id, action = 'buy'),
    }
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
        'all_data': NFT.objects.filter(owner=str(request.user)),
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
    """Function line."""
    context = {}
    if request.method == 'POST':
        try:
            make = request.POST.get('make')
        except:
            pass
    print(make)
    if int(make):
        trade_time = time.time()
        query = get_object_or_404(NFT, id=make)
        print(int(0.7*query.price),int(1.3*query.price))
        context.update({
        'page' :  'trades',
        'nft_price_l' : int(0.7*query.price),
        'nft_price_h' : int(1.3*query.price),
        'nft_price' : int(query.price),
        'nft_name' : str(query.name),
        'time' : str(trade_time),
        'owner' : str(query.owner),
        'user' : str(request.user)
        })
        response = render(request, 'make_trade.html', context)
        request.session['nft_id'] = str(make)
        return response


@login_required
def my_trades_page(request):
    """Function line."""
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
    make = request.session.get('nft_id')
    if request.method == 'POST':
        query = get_object_or_404(NFT, id = int(make))
        if str(request.user) == str(query.owner):
            sec = time.time()
            query.in_market='true'
            query.save()
            struct = time.localtime(sec)
            trade_time = time.strftime('%d.%m.%Y %H:%M', struct)
            text = request.POST.get('message')
            trade_price = request.POST.get('trade_price')
            trade = Trade(action = 'sale' , id_nft=query.id, price_array=trade_price, chat='', owner = str(query.owner), new_owner=str(request.user), time= trade_time)
            trade.save()
            context.update({'text': 'operation compleate!!!!'})
        else:
            sec = time.time()
            struct = time.localtime(sec)
            trade_time = time.strftime('%d.%m.%Y %H:%M', struct)
            query = get_object_or_404(NFT, id = int(make))
            text = request.POST.get('message')
            trade_price = request.POST.get('trade_price')
            trade = Trade(action = "buy", id_nft=query.id, price_array=trade_price, chat=text, owner = str(query.owner), new_owner=str(request.user), time= trade_time )
            trade.save()
            context.update({'text': 'operation compleate!!!!'})
        return render(request, 'transaction.html', context)
    if request.method == 'GET':
        trade = request.GET.get('trade_id')
        person = get_object_or_404(CustomUser, username=request.user)
        if trade:
            t_ass = get_object_or_404(Trade, id=trade)
            arr = []
            new_owner_nft = get_object_or_404(CustomUser, username=t_ass.new_owner)
            ass = get_object_or_404(NFT, id=t_ass.id_nft)
            if  person.username == str(ass.owner):
                person.balance+=t_ass.price_array
                new_owner_nft.balance-=t_ass.price_array
                ass.in_market='false'
                ass.owner=str(new_owner_nft.username)
                person.save()
                new_owner_nft.save()
                ass.save()
                print(ass.id)
                arr = Trade.objects.filter(id_nft=int(ass.id))
                print(2)
                arr.delete()
                #t_ass.delete()
                print(1)
                context.update({
                    'text': 'operation compleate!!!!'})
    return render(request, 'transaction.html', context)

@login_required
def create_page(request):
    """Function line."""
    context = {
        'page': 'create'
    }
    return render(request, 'create_NFT.html', context)
