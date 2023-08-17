from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Mantra(TimeStamp):
    name = models.CharField(max_length=1000,verbose_name='Name of Mantra')
    banner_image = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name='Banner Image')
    exact_mantra = models.TextField(null=True,blank=True,verbose_name='Exact Mantra')
    description = models.TextField(null=True,blank=True,verbose_name='Description meaning of Mantra')
    link = models.CharField(max_length=1000,null=True,blank=True,verbose_name='Link of audio file')
    loop_count = models.IntegerField(default=0,verbose_name='Loop Count of Mantra')
    views_count = models.IntegerField(default=0,verbose_name='Views Count of Mantra')
    


    class Meta:
        verbose_name_plural = 'Mantra Haru'
    
    def __str__(self):
        return self.name


