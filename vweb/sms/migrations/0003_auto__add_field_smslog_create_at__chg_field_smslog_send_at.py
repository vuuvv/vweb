# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SMSLog.create_at'
        db.add_column('sms_smslog', 'create_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 1, 14, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'SMSLog.send_at'
        db.alter_column('sms_smslog', 'send_at', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):
        # Deleting field 'SMSLog.create_at'
        db.delete_column('sms_smslog', 'create_at')


        # Changing field 'SMSLog.send_at'
        db.alter_column('sms_smslog', 'send_at', self.gf('django.db.models.fields.DateTimeField')(default=1))

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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sms']