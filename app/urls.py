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
    path('proedit',profileedit,name='proedit'),
    path('addbook',addbook,name='addbook'),
    path('viewbook/<int:bid>',viewbook,name='viewbook'),
    path('deletebook/<int:bid>',deletebook,name='deletebook'),
    path('editbook/<int:bid>',editbook,name='editbook'),
    path('addauthor',addauthor,name='addauthor')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)