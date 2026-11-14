from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home',homepage,name='home'),
    path('register',registerpage,name='register'),
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name="logout"),
    path('dash',dashboard,name='dash'),
    path('manage',managepage,name='manage'),
    path('profile',profilepage,name='profile'),
    path('proedit',profileedit,name='proedit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)