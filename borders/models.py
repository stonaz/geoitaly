from django.contrib.gis.db import models

class ProvBorder(models.Model):
    cod_reg = models.IntegerField()
    cod_pro = models.IntegerField()
    nome_pro = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    
    objects = models.GeoManager()

    class Meta:
        ordering = ['nome_pro']
    
    
    def __unicode__(self):
        return self.nome_pro
    
    
class ComuniBorder(models.Model):
    cod_reg = models.IntegerField()
    cod_pro = models.IntegerField()
    pro_com = models.IntegerField()
    nome_com = models.CharField(max_length=58)
    nome_ted = models.CharField(max_length=100)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.nome_com



   
