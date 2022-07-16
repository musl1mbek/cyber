
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Api.url')),
    path('', Login_funk,name = 'login'),
    path('adminlar/', Admin_Page, name='admin'),

    #delete 
    path('delete-info/<int:pk>/', Delete_Info,name = 'delete-info'),
    path('delete-mission/<int:pk>/', Delete_Mission,name ='delete-mission'),
    path('delete-menu/<int:pk>/', Delete_Menu,name ='delete-menu'),
    path('introductory_delete/<int:pk>/', Introductory_Delete,name ='introductory_delete'),
    path('delete-games/<int:pk>/', Delete_Games,name ='delete-games'),
    path('delete-player/<int:pk>/', Delete_Player,name ='delete-player'),
    path('delete-team/<int:pk>/', Delete_Team,name ='delete-team'),
    path('delete-turnir/<int:pk>/', Delete_Turnir,name ='delete-turnir'),
    path('delete-one_vs_one/<int:pk>/', Delete_One_Vs_One,name ='delete-one_vs_one'),
    path('delete-images/<int:pk>/', Delete_Img_Gallery,name ='delete-img_gallery'),
    path('delete-strimers/<int:pk>/', Delete_Strimers,name ='delete-strimers'),
    path('delete-email/<int:pk>/', Delete_Emails,name ='delete-email'),
    path('test/', test)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
