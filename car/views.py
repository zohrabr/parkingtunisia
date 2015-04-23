# -*- coding: utf-8 -*-
from __future__ import division
from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from car.models import  parking, User, owner
from car.forms import  parkingform , userform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login, logout, authenticate 
from geoposition import Geoposition
import json
from django.core.serializers.json import DjangoJSONEncoder


def register(request):
	context = RequestContext(request)
	registred = False
	if request.method =='POST' :
		
		owner_form = userform(data= request.POST)	
		if owner_form.is_valid():
			
			propr = owner_form.save(commit=False)
			propr.set_password(propr.password)
			
			if 'teleport' in request.FILES:
				propr.teleport =request.FILES['teleport']
			propr.save()
			registred = True 
			return render_to_response('car/merci.html',{},context)
		else :
			print owner_form.errors
	else:
		
		owner_form= userform()
		
	return render_to_response('car/register.html',{'user_form':owner_form, 'registred': registred}, context)






 
def accueil(request):
	context = RequestContext(request)
	return render_to_response('car/index.html',{},context)



def user_login(request):
	context= RequestContext(request)
	if request.method == 'POST':		
		mail= request.POST['email']
		userpass = request.POST['password']
		try:
			userf= User.objects.get(email = mail)
			usern= userf.username
			user = authenticate(username=usern,password=userpass)		
			if user :
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/car/')
				else:
					return HttpResponse("votre compte est désactivé")
			else:
					return render_to_response('car/erreurlogin.html', {}, context)
		except User.DoesNotExist:	
			return render_to_response('car/erreurlogin.html', {}, context)
	else:
			return render_to_response('car/login.html', {}, context)



@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/car/')



@login_required
def add_parking(request):
	context=RequestContext(request)
	if request.user is not None:
    		own = owner.objects.get(username=request.user.username)	
	if request.method == 'POST':
		form= parkingform(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.proprietaire=own
			if 'site' in request.FILES :
				form.site=request.FILES['site']
			form.save()
			return accueil(request)
		else:
			print form.errors
	else:
		form = parkingform()
	return render_to_response('car/add_parking.html',{'form' : form }, context)

@login_required
def list_park_owner(request):
	context   =  RequestContext(request)
	if request.user is not None:
		ownercon = owner.objects.get(username=request.user.username)
	list_park=parking.objects.filter(proprietaire=ownercon)
	return render_to_response('car/list_parking.html',{'list_park':list_park},context)


@login_required
def supprimer(request):
	context=RequestContext(request)
	if request.user is not None:
		own=owner.objects.get(username=request.user.username)
	if request.method=='POST':
		nom=request.POST['name']
		try:
			p=parking.objects.get(proprietaire=own,namepark=nom)
			p.delete()
			return accueil(request)
		except parking.DoesNotExist :				
			return render_to_response('car/vide.html',{},context)
	else:
		return render_to_response('car/delete.html',{}, context)

def carte(request):
    return render(request, 'car/carte.html', locals())


def filterpark(request):
    if request.method == "GET":
        park = parking.objects.filter(accept=True)
        park = list(park.values_list("namepark", "position","nbplacevide","nbrplace","telephone","genre"))
        return HttpResponse(json.dumps(park, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        return HttpResponse()
@login_required
def gerer(request):
	context   =  RequestContext(request)
	if request.method == "GET":
		if request.user is not None:
			ownercon = owner.objects.get(username=request.user.username)
		list_park=parking.objects.filter(proprietaire=ownercon, accept=True)
	
	elif request.method == "POST":
		if request.user is not None:
			ownercon = owner.objects.get(username=request.user.username)
		list_park=parking.objects.filter(proprietaire=ownercon, accept=True)
		for i in list_park :
			nbpv = str(i.id)
			f=request.POST[nbpv]
			i.nbplacevide =f
			i.save()
		return accueil(request)

	return render_to_response('car/gerer_parking.html',{'list_park':list_park},context)	

def filterParkings(request):	
	listpark= parking.objects.filter(accept=True)
	l=[]	
	lista=[]
	filter_parking=[]
	if request.method =='GET':
		if 'top' not in request.GET or 'bottom' not in request.GET or 'left' not in request.GET  or 'right' not in request.GET: #this line gave me cancer !
			print" returning regular list"
			return filterpark(request)

		top 	= float(request.GET['top'])
		bottom 	= float(request.GET['bottom'])
		left 	= float(request.GET['left'])
		right 	= float(request.GET['right'])

		for i in listpark:
			c = i.position.latitude
			d = i.position.longitude
			if (d <= right ) and (d >= left) and (c >= bottom) and (c <= top) :
				l.append(i.id)
		for j in l :
			p= parking.objects.get(id=j)
			lista.append(p)
		lon = len(lista)
		for j in range(0,lon) :	
			h={
				"name" 	: 		lista[j].namepark,
				"adresse" :		lista[j].place,
				"telephone" :	lista[j].telephone,
				"empty_places": lista[j].nbplacevide,
				"places_count": lista[j].nbrplace,
				"hour_price" : 	lista[j].genre,
				"lat"  : 		lista[j].position.latitude,
				"long" : 		lista[j].position.longitude
			}
			filter_parking.append(h)
		print filter_parking
		return HttpResponse(json.dumps(filter_parking), content_type="application/json")
	else:
		return HttpResponse()
		
