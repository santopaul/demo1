from django.db import models

# Create your models here.
class portfolio_status(models.Model): 
    title=models.CharField(max_length=300)
    status=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    det_date=models.CharField(max_length=50)
    available=models.BooleanField(default=True)
    category=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    img_vid=models.BooleanField(default=False)
    img=models.ImageField(upload_to='assets/images/',null=True)
    vid=models.FileField(upload_to='assets/videos/',null=True)
    
    
class portfolio_work(models.Model):
    title=models.CharField(max_length=300)
    status=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    img_vid=models.BooleanField(default=False)
    img=models.ImageField(upload_to='assets/images/',null=True)
    vid=models.FileField(upload_to='assets/videos/',null=True)
    
    
class people_about(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    img=models.ImageField(upload_to='assets/images/',null=True)
    
 
class home_portfolio_status(models.Model):
    det_date=models.CharField(max_length=50)
    anytext=models.CharField(max_length=300)
    category=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    img_vid=models.BooleanField(default=False)
    img=models.ImageField(upload_to='assets/images/',null=True)
    vid=models.FileField(upload_to='assets/videos/',null=True)


class home_portfolio_work(models.Model):
    title=models.CharField(max_length=300)
    status=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    img_vid=models.BooleanField(default=False)
    img=models.ImageField(upload_to='assets/images/',null=True)
    vid=models.FileField(upload_to='assets/videos/',null=True)