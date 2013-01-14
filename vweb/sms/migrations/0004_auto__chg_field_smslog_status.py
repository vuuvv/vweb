# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SMSLog.status'
        db.alter_column('sms_smslog', 'status', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'SMSLog.status'
        db.alter_column('sms_smslog', 'status', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'sms.smscontent': {
            'Meta': {'object_name': 'SMSContent'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'sms.smslog': {
            'Meta': {'object_name': 'SMSLog'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sms.SMSContent']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'request_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sms']