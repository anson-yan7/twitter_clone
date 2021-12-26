"""twitter192 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core.views import splash, signup, login_view, home, post, like, profile, hashtag, logout, hashtaglike, delete, \
    hashtagdelete

urlpatterns = [
    path('', splash, name='splash'),
    path('hashtag/<str:tag>', hashtag, name='hashtag'),
    path('logout/', logout, name='logout'),
    path('tw/', post, name='post'),
    path('signup/', signup, name='signup'),
    path('login/', login_view),
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('like/<id>', like, name="like"),
    path('profile/<str:id>', profile, name='profile'),
    path('home/like/<id>', like, name="like"),
    path('profile/like/<id>', like, name="like"),
    path('hashtag/like/<id>/<tag>', hashtaglike, name="like"),
    path('home/delete/<id>', delete, name='delete'),
    path('profile/delete/<id>', delete, name='delete'),
    path('hashtag/delete/<id>/<tag>', hashtagdelete, name='delete'),


    # path('post/<str:id>', post, name='post')

]
