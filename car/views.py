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
			return HttpResponse("<strong>votre @email et/ou mot de passe sont incorrectes !</strong>")
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
        park = list(park.values_list("namepark", "position","nbplacevide","nbrplace","telephone"))
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
			f = request.POST[nbpv]
			i.nbplacevide = f
			i.save()
			
	return render_to_response('car/gerer_parking.html',{'list_park':list_park},context)		

			
		

