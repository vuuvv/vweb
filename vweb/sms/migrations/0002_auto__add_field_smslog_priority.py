# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SMSLog.priority'
        db.add_column('sms_smslog', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SMSLog.priority'
        db.delete_column('sms_smslog', 'priority')


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
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'request_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sms']