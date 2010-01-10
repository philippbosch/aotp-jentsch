from django.db import models
from django.utils.translation import ugettext_lazy as _

class Track(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    audio_file = models.FileField(verbose_name=_("Audio File"), upload_to="uploads/audio/")
    image_file = models.ImageField(verbose_name=_("Image File"), upload_to="uploads/images/")
    order = models.PositiveSmallIntegerField(verbose_name=_("Order"), blank=True, default=0)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('order',)