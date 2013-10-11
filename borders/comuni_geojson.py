import simplejson as json
from models import ComuniBorder

comuni_geojson = {
    "type": "FeatureCollection",
  "features": []
}


comuni_roma=ComuniBorder.objects.filter(cod_pro=58)

def run():

    for comune in comuni_roma:
        comuni_features = { "type": "Feature",
                    "geometry": {"type": "MultiPolygon", "coordinates": []},
                    "properties": {"name": ""},
                    "properties": {"id": ""}
}
        #print(comune.nome_com)
        print comune
        comuni_features["properties"]["id"] = comune.id
        comuni_features["properties"]["name"] = comune.nome_com
        comuni_features["geometry"] = comune.geom.geojson
        comuni_geojson["features"].append(comuni_features)
    s=json.dumps(comuni_geojson).replace("\\", "")
    s=s.replace("\"{", "{")
    s=s.replace("}\"", "}")
    f=open("test.geojson",'w')
    f.write(s)
    
  


