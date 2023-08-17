from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class PoojaBidhi(TimeStamp):
    name  = models.CharField(max_length=1000,verbose_name='Name of Pooja Bidhi')
    banner_image = models.ImageField(upload_to='images/',null=True,blank=True,verbose_name='Banner Image')
    exact_poojabidhi = models.TextField(null=True,blank=True,verbose_name='Exact Pooja Bidhi')
    description = models.TextField(null=True,blank=True,verbose_name='Description meaning of Pooja Bidhi')
    link = models.CharField(max_length=1000,null=True,blank=True,verbose_name='Link of audio file')
    loop_count = models.IntegerField(default=0,verbose_name='Loop Count of Pooja Bidhi')
    views_count = models.IntegerField(default=0,verbose_name='Views Count of Pooja Bidhi')
    


    class Meta:
        verbose_name_plural = 'Pooja Bidhi Haru'
    
    def __str__(self):
        return self.name



