"""Import line"""
from website.models import NFT
from website.forms import RegisterUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView


class DataMixin:
    """Class line"""

    def __init__(self):
        """Function line"""
        self.context = 0

    def get_user_context(self, **kwargs):
        """Function line"""
        self.context = kwargs
        if 'cat_selected' not in self.context:
            self.context['cat_selected'] = 0
        return self.context


class RegUser(DataMixin, CreateView):
    """Class line"""
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, kwargs: object):
        """Function line"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Reg')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    """Class line"""
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, kwargs: object):
        """Function line"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign_in')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    """Function line"""
    logout(request)
    return redirect('/')

# Create your views here.


def main_page(request):
    """Function line"""
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
    """Function line"""
    context = {'page': 'create'}
    return render(request, 'login.html', context)


def data_post_id(request, post_id):
    """Function line"""
    query = get_object_or_404(NFT, id=post_id)
    context = {'form': query}
    return render(request, 'one_nft.html', context)


def profile_page(request):
    """Function line"""
    context = {'page': 'profile', 'height': '20'}
    return render(request, 'profile.html', context)


def game_page(request):
    """Function line"""
    context = {'height': '40', 'page': 'game'}
    return render(request, 'game.html', context)


def inventory_page(request):
    """Function line"""
    ass = NFT.objects.filter(owner=str(request.user))
    context = {'all_data': ass, 'height': '40'}
    return render(request, 'market.html', context)


def clicker_page(request):
    """Function line"""
    context = {'page': 'clicker'}
    return render(request, 'clicker.html', context)


def market_page(request):
    """Function line"""
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
    """Function line"""
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
    """Function line"""
    context = {

        'page': 'create'

    }

    return render(request, 'create_NFT.html', context)
