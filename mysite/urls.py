"""mysite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from website import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', views.profile_page),
    path('inventory/', views.inventory_page, name='inventory'),
    path('trade/', views.trade_page, name='trade'),
    path('trades/', views.my_trades_page, name='trades'),
    path('market/<int:post_id>', views.data_post_id),
    path('', views.main_page, ),
    path('market/', views.market_page, name='market'),
    path('create/', views.create_page),
    path('clicker/', views.clicker_page, name='clicker'),
    path('registory/', views.RegUser.as_view()),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user),
    path('transaction/', views.transaction),
    path('game/', views.game_page, name='game'),
] + static(settings.NFT_URL, document_root=settings.NFT_ROOT)
