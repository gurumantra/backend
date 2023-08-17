from django.db import models

from mantra.models import TimeStamp

class ChadParba(TimeStamp):
    name = models.CharField(max_length=1000,verbose_name='Name of Chad Parba')
    date_of_chad_ad = models.DateField(null=True,blank=True,verbose_name='Date of Chad Parba')
    short_description = models.TextField(null=True,blank=True,verbose_name='Short Description of Chad Parba')
    preview_image = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name='Preview Image')
    related_mantra = models.ManyToManyField('mantra.Mantra',blank=True,verbose_name='Related Mantra')
    related_poojabidhi = models.ManyToManyField('poojabidhi.PoojaBidhi',blank=True,verbose_name='Related Pooja Bidhi')
    related_chadparba = models.ManyToManyField('self',blank=True,verbose_name='Related Chad Parba')
    views_count = models.IntegerField(default=0,verbose_name='Views Count of Chad Parba')

    class Meta:
        verbose_name_plural = 'Chad Parba Haru'
    
    def __str__(self):
        return self.name
    
  
    @property
    def is_today(self):
        from datetime import date
        if self.date_of_chad_ad == date.today():
            return True
        else:
            return False
    
    @property
    def is_upcoming(self):
        from datetime import date
        if self.date_of_chad_ad > date.today():
            return True
        else:
            return False
    
    @property
    def is_past(self):
        from datetime import date
        if self.date_of_chad_ad < date.today():
            return True
        else:
            return False
