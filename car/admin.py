from django.contrib import admin
from car.models import parking , owner,User

# Register your models here.
class Park(admin.ModelAdmin):
	 list_display = ('namepark', 'nbrplace','proprietaire','accept')
class use(admin.ModelAdmin):
	 list_display=('username', 'first_name','last_name','teleport')
	

admin.site.register(parking,Park)
admin.site.register(owner,use)

