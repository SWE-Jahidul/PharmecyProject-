
from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginPage, name = 'loginpage'),
    path('manage/', views.controlpanel, name='manage'),
    path('add/', views.add,name='add'),
    path('sale/', views.sale,name='sale'),
    path('category/', views.category, name='category'),
    path('generic/', views.generic, name='generic'),
    path('mdetails/<int:mid>', views.mdetails, name='mdetails'),
    path('medicine/', views.medicine, name='medicine'),
    path('logout', views.logoutNow, name ='logoutpage')
]

