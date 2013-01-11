# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SMSContent'
        db.create_table('sms_smscontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('sms', ['SMSContent'])

        # Adding model 'SMSLog'
        db.create_table('sms_smslog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sms.SMSContent'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('request_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('send_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('sms', ['SMSLog'])


    def backwards(self, orm):
        # Deleting model 'SMSContent'
        db.delete_table('sms_smscontent')

        # Deleting model 'SMSLog'
        db.delete_table('sms_smslog')


    models = {
        'sms.smscontent': {
            'Meta': {'object_name': 'SMSContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sms.smslog': {
            'Meta': {'object_name': 'SMSLog'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sms.SMSContent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'request_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sms']