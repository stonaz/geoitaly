import os
from django.contrib.gis.utils import LayerMapping
from models import ComuniBorder

provborder_mapping = {
    'cod_reg' : 'COD_REG',
    'cod_pro' : 'COD_PRO',
    'nome_pro' : 'NOME_PRO',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}


prov2011_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/prov2011.shp'))

def run(verbose=True):
    lm = LayerMapping(ProvBorder, prov2011_shp, provborder_mapping,
                      transform=True, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
