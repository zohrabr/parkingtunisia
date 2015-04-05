# -*- coding: utf-8 -*-
from car.models import parking, owner
from django import forms
from django.contrib.auth.models import User


genr=(
	('payant','payant'),
	('gratuit','gratuit'),
)
class userform(forms.ModelForm):
	 last_name =forms.CharField(help_text="Nom:")
	 first_name = forms.CharField(help_text="Prénom:")
	 username = forms.CharField(help_text="Identité (CIN):")
         email = forms.CharField(help_text=" Email")
         password = forms.CharField(widget=forms.PasswordInput(), help_text="Mot de passe:")
	 teleport=forms.CharField(max_length = 15,help_text="Téléphone:")
	 class Meta:
		model = owner
		fields=['last_name','first_name','username','password','email','teleport']



class parkingform(forms.ModelForm):
	namepark  = forms.CharField(max_length = 30, help_text="Nom du parking :")	
	nbrplace  = forms.IntegerField( help_text="Nombre total de place :")
	place     = forms.CharField(max_length=200, help_text="Adresse :")
	telephone = forms.CharField(max_length = 15,help_text="Téléphone")
	genre	  = forms.ChoiceField(widget=forms.RadioSelect, choices=genr, help_text=' ')
	class Meta:
		model = parking
		fields=['namepark','nbrplace','place','genre','telephone','position']

