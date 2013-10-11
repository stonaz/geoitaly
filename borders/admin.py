from django.contrib.gis import admin

from models import ProvBorder,ComuniBorder

class ComuniBorderAdmin(admin.OSMGeoAdmin):
    search_fields = ['nome_com']
    list_filter = ['cod_pro']
    
class ProvBorderAdmin(admin.OSMGeoAdmin):
    search_fields = ['nome_pro']

admin.site.register(ComuniBorder, ComuniBorderAdmin)
admin.site.register(ProvBorder, ProvBorderAdmin)