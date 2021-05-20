from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class University(models.Model):
    universityid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return "Name: {}, Address: {}".format(self.name, self.address)

class Interests(models.Model):
    interestId = models.IntegerField(primary_key=True)
    interest = models.CharField(max_length=100)

    def __str__(self):
        return "Interest: {}".format(self.interest)

class List(models.Model):
    listId = models.IntegerField(primary_key=True)
    listName= models.CharField(max_length=200)
    
    def __str__(self):
        return "List name: {}".format(self.listName)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    isCandidate = models.BooleanField(default=False)
    studentIdNumber = models.CharField(max_length=11)
    faculty = models.CharField(max_length=200)
    DoB = models.DateField(null=True,blank=True)
    university = models.ForeignKey(University,on_delete=models.CASCADE,db_column='university', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Candidate(models.Model):
    candidateId = models.IntegerField(primary_key=True)
    profileId = models.ForeignKey(Profile,on_delete=models.CASCADE)
    interestsId = models.ForeignKey(Interests,on_delete=models.CASCADE)
    listId = models.ForeignKey(List,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='cars')
    aboutMe = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.aboutMe)

    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
