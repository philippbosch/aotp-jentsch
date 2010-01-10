
from south.db import db
from django.db import models
from music.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Track'
        db.create_table('music_track', (
            ('id', orm['music.Track:id']),
            ('name', orm['music.Track:name']),
            ('audio_file', orm['music.Track:audio_file']),
            ('image_file', orm['music.Track:image_file']),
            ('order', orm['music.Track:order']),
        ))
        db.send_create_signal('music', ['Track'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Track'
        db.delete_table('music_track')
        
    
    
    models = {
        'music.track': {
            'audio_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }
    
    complete_apps = ['music']
