from django.contrib import admin
from .models import *
# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_display_links = ('title',)
class DocAdmin(admin.ModelAdmin):
    list_display = ('id','datadoc','nomerdoc','transaction','dealer','created_at','updated_at')
    list_display_links = ('id', 'datadoc', 'nomerdoc', 'transaction', 'dealer', 'created_at', 'updated_at')
class DocJurnalAdmin(admin.ModelAdmin):
    list_display = ('iddoc','title','volume','buyprice','percent','saleprice', 'buytotal','saletotal')
    list_display_links = ('iddoc','title','volume','buyprice','percent','saleprice', 'buytotal','saletotal')
admin.site.register(Good)
admin.site.register(Unit,UnitAdmin)
admin.site.register(DocJurnal,DocJurnalAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Dealer)
admin.site.register(Operator)
admin.site.register(Pay)
admin.site.register(Doc,DocAdmin)

admin.site.register(Operation)