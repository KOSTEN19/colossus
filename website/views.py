"""Import line."""
from user.models import *
from website.models import NFT
from website.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
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
            description=description)
        nft.save()
    return render(request, 'main.html', context)


def login_page(request):
    """Function line."""
    context = {'page': 'create'}
    return render(request, 'login.html', context)


def data_post_id(request, post_id):
    """Function line."""
    query = get_object_or_404(NFT, id=post_id)
    context = {'form': query}
    return render(request, 'one_nft.html', context)


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


def game_page(request):
    """Function line."""
    context = {'height': '40', 'page': 'game'}
    return render(request, 'game.html', context)


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


def clicker_page(request):
    """Function line."""

    if request.method == 'POST':
        player = get_object_or_404(CustomUser, username=request.user)
        player.balance += min(100000, abs(int((request.POST.get('balance')))))
        player.save()
    context = {'page': 'clicker'}
    return render(request, 'clicker.html', context)


def market_page(request):
    """Function line."""
    context = {
        'all_data': NFT.objects.all().exclude(owner=str(request.user)),
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


def transaction(request):
    """Function line."""
    context = {}
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
                ass.owner=''
                ass.save()
                person.balance+=int(ass.price)
                person.save()
                context.update({
                    'text': 'transaction compleate!!!!'})
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
                print(person.balance)
                print(person.balance)
                person.balance -= int(ass.price)
                person.save()
                print(person.balance)
                ass.owner = str(request.user)
                ass.save()
                context.update({
                    'text': 'transaction compleate!!!!'})
            else:
                context.update({
                    'text': 'Not enought money or it is yours :('})
    return render(request, 'transaction.html', context)


def create_page(request):
    """Function line."""
    context = {
        'page': 'create'
    }
    return render(request, 'create_NFT.html', context)
