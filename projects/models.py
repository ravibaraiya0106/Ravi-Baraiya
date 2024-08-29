from django.db import models

# Create your models here.

class Info(models.Model):
    logo = models.ImageField(blank=True, null=True, upload_to='media')
    photo = models.ImageField(blank=True, null=True, upload_to='media')
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    resume = models.FileField(blank=True, null=True, upload_to='media')
    total_projects = models.IntegerField(null=True)

    def __str__(self):
        return f"My Information"


class Skills(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, null=True, upload_to='media')

    def __str__(self):
        return f"{self.name}"

class Links(models.Model):
    github = models.TextField()
    linkedin = models.TextField()
    twitter = models.TextField()
    facebook = models.TextField()
    instagram = models.TextField()

    def __str__(self):
        return f"Social Media Links"

    
class Experience(models.Model):
    years = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    comany_name = models.CharField(max_length=100, null=True)
    desc = models.TextField()

    def __str__(self):
        return f"{self.comany_name}"

class Projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True, upload_to='media')
    codelink = models.TextField()
    livelink = models.TextField()

    def __str__(self):
        return f"{self.name}"
