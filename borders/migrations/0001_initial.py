# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProvBorder'
        db.create_table(u'borders_provborder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_reg', self.gf('django.db.models.fields.IntegerField')()),
            ('cod_pro', self.gf('django.db.models.fields.IntegerField')()),
            ('nome_pro', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'borders', ['ProvBorder'])

        # Adding model 'ComuniBorder'
        db.create_table(u'borders_comuniborder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_reg', self.gf('django.db.models.fields.IntegerField')()),
            ('cod_pro', self.gf('django.db.models.fields.IntegerField')()),
            ('pro_com', self.gf('django.db.models.fields.IntegerField')()),
            ('nome_com', self.gf('django.db.models.fields.CharField')(max_length=58)),
            ('nome_ted', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'borders', ['ComuniBorder'])


    def backwards(self, orm):
        # Deleting model 'ProvBorder'
        db.delete_table(u'borders_provborder')

        # Deleting model 'ComuniBorder'
        db.delete_table(u'borders_comuniborder')


    models = {
        u'borders.comuniborder': {
            'Meta': {'object_name': 'ComuniBorder'},
            'cod_pro': ('django.db.models.fields.IntegerField', [], {}),
            'cod_reg': ('django.db.models.fields.IntegerField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_com': ('django.db.models.fields.CharField', [], {'max_length': '58'}),
            'nome_ted': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pro_com': ('django.db.models.fields.IntegerField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {})
        },
        u'borders.provborder': {
            'Meta': {'ordering': "['nome_pro']", 'object_name': 'ProvBorder'},
            'cod_pro': ('django.db.models.fields.IntegerField', [], {}),
            'cod_reg': ('django.db.models.fields.IntegerField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_pro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['borders']