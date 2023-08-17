from django.db import models
from mantra.models import TimeStamp

class Katha(TimeStamp):
    name = models.CharField(max_length=1000,verbose_name='Name of Katha')
    thumbnail = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name='Thumbnail Image')
    description = models.TextField(null=True,blank=True,verbose_name='Description meaning of Katha')
    youtube_link = models.CharField(max_length=1000,null=True,blank=True,verbose_name='Link of youtube video')
    views_count = models.IntegerField(default=0,verbose_name='Views Count of Katha')
    tag = models.CharField(max_length=1000,null=True,blank=True,verbose_name='Tag of Katha')
    realted_katha = models.ManyToManyField('self',blank=True,verbose_name='Related Katha')
    realted_chadparba = models.ManyToManyField('chadparba.Chadparba',blank=True,verbose_name='Related Chadparba')
    

    class Meta:
        verbose_name_plural = 'Katha Haru'
    
    def __str__(self):
        return self.name
