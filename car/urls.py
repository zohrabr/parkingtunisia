 
from django.conf.urls import  patterns, url
from car import views



urlpatterns=patterns('', 
	url(r'^inscription/$', views.register , name='inscription'),# create account
	url(r'^$', views.accueil , name='accueil'), #home page
	url(r'^login/$', views.user_login , name='login'),
	url(r'^logout/$', views.user_logout , name='logout'),
	url(r'^add_parking/$', views.add_parking , name='ajout'), #parking owner --> add parking
	url(r'^my_parking_list/$', views.list_park_owner),#afficher la liste des parking pour chaque proprietaire
	url(r'^delete/$', views.supprimer ),#supprimer
	url(r'^carte/$', views.carte),
	url(r'^liste/$',views.filterpark),
	url(r'^gerer/$',views.gerer),
	url(r'^listmobile/',views.mobile),
)
