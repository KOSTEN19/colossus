"""Import line."""
import time
from click import edit
import numpy as np
from PIL import Image, ImageChops
from website.models import NFT, Trade_sell, Trade_buy
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
    edit = 0
    try:
        edit = request.session.get('edit_id')
    except: pass
    print(edit)
    if edit!=None:
        print(edit,'-----')
        print('in asss')
        description = request.POST.get('description')
        print(description)
        nft = get_object_or_404(NFT, id= edit)
        nft.description=str(description)
        nft.save()
        del request.session['edit_id']
        return redirect('/inventory/')

    elif request.method == 'POST':
        namenft = request.POST.get('name')
        pricenft = request.POST.get('price')
        nftimage = request.FILES.get('myfile')
        description = request.POST.get('description')
        count = request.POST.get('count')
        im = None
        try:
           im= Image.open(nftimage)
        except :
            return redirect('/create/')
        im = im.size
        if int(im[0])-int(im[1]) > 0.01*im[0]:
            messages.error(request, 'Image is not rect!! ')
            return redirect('/create/')

        print(im)
        print('make')
        data = NFT.objects.all()
        unique = True
        if len(data) > 0:
            for i in data:
                im1 = Image.open(nftimage).convert('RGB')
                im2 = Image.open(i.image).convert('RGB')
                raz = calcdiff(im1, im2)
                if raz < 15 or namenft == i.name:
                    unique = False
                    print(raz, unique)
        if unique:
            print('unique')
            for i in range(abs(int(count))):
                try:
                    nft = NFT(
                        image=nftimage,
                        name=namenft,
                        price=abs(int(pricenft)),
                        description=description,
                        owner=request.user,
                        id_in_arr=i,
                        in_market = False,
                        author = str(request.user),
                        count=int(count))
    
                    nft.save()
                except BaseException:
                    return redirect('/create/')
        if unique:
            return redirect('/inventory/')
        else:
            messages.error(request, 'NFT is not unique!!!')
            print('here')
            return redirect('/create/')
    else:print('BAN')
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
               'all_data': Trade_buy.objects.filter(id_nft=post_id),
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
        except:
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
        'all_data': Trade_sell.objects.all(),
        # .exclude(owner=str(request.user))
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
    if int(make):
        query = get_object_or_404(NFT, id=make)
        if str(request.user) == str(query.owner):
            context.update({
                'page': 'trades',
                'nft_price_l': int(0.7 * query.price),
                'nft_price_h': int(1.3 * query.price),
                'nft_price': int(query.price),
                'nft_name': str(query.name),
                'time': str(get_time()),
                'owner': str(query.owner),
                'user': str(request.user)
            })
          #  trade = get_object_or_404(Trade_sell, id_nft=make)
        elif str(request.user) != str(query.owner):
            trade = get_object_or_404(Trade_sell, id_nft=make)
            context.update({
                'page': 'trades',
                'nft_price_l': min(int(request.user.balance),int(0.7 * trade.new_price)),
                'nft_price_h': min(int(request.user.balance),int(1.3 * trade.new_price)),
                'nft_price': int(trade.new_price),
                'nft_name': str(trade.name),
                'time': str(get_time()),
                'owner': str(trade.owner),
                'user': str(request.user)
            })
        response = render(request, 'make_trade.html', context)
        request.session['nft_id'] = str(make)
        return response


@login_required
def my_trades_page(request):
    """Function line."""
    context = {
        'all_data': Trade.objects.filter(new_owner=str(request.user)),
        'page': 'trades',
        'height': '40'
    }
    return render(request, 'my_trades.html', context)
def get_time():
    sec = time.time()
    struct = time.localtime(sec)
    return time.strftime('%d.%m.%Y %H:%M', struct)

@login_required
def transaction(request):
    """Function line."""
    context = {}
    make = request.session.get('nft_id')
    query = get_object_or_404(NFT, id=int(make))

    if request.method == 'POST':
        try:
            #edit_id = request.POST.get('edit_id')
            trade_price = request.POST.get('trade_price')
            trade_id = request.POST.get('trade_id')
        except: pass
        if trade_id != None:
            trade_buy = get_object_or_404(Trade_buy,id=trade_id)
            trade_sell = get_object_or_404(Trade_sell, id_nft = query.id)
            buyer = get_object_or_404(CustomUser, username=trade_buy.author)
            request.user.balance+=abs(trade_buy.new_price)
            buyer.balance-=abs(trade_buy.new_price)
            query.owner=buyer.username
            query.in_market=False
            arr = Trade_buy.objects.filter(id_nft=query.id)
            arr.delete()
            trade_sell.delete()
            query.save()
            buyer.save()
            request.user.save()

        elif str(request.user) == str(query.owner) and query.in_market==False: # если владелец
            query.in_market=True
            query.save()
            trade = Trade_sell(
                owner_image = request.user.profile_pic,
                image = query.image,
                name = query.name,
                price = query.price,
                author = query.author,
                description = query.description,
                owner=query.owner,
                id_in_arr = query.id_in_arr,
                id_nft = query.id,
                count = query.count,
                new_price=trade_price,
                in_market= query.in_market,
                time = get_time())

            trade.save()
        elif str(request.user) != str(query.owner):
            text = request.POST.get('message')
            trade = Trade_buy(
                id_nft=query.id,
                new_price=min(request.user.balance,abs(int(trade_price))),
                message=text,
                author=request.user,
                time=get_time())
            trade.save()
     
            context.update({'text': 'operation compleate!!!!'})

    return render(request, 'transaction.html', context)


@login_required
def create_page(request):
    """Function line."""
    context = {
        'page': 'create',
        }
    edit_id = 0
    print('---------')
    if request.method == 'POST':
        edit_id = request.POST.get('edit_id')
        print('---------')
        print(edit_id)
        print('---------')
        nft = get_object_or_404(NFT, id = int(edit_id))
        
        request.session['edit_id'] = nft.id
        context.update({
        'page': 'create',
        'nft': nft,
        'edit': True,
    })
    response = render(request, 'create_NFT.html', context)
    return response
