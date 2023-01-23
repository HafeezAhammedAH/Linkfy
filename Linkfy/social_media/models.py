from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=200,null=True)
    following=models.ManyToManyField(User)
    timeline_pic=models.ImageField(upload_to="timelinepics",null=True)
    
    def __str__(self):
        return self.bio

class Posts(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userpost")
    caption=models.CharField(max_length=200)
    image=models.ImageField(upload_to="postimage",null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=250)
    liked_by=models.ManyToManyField(User)

    def __str__(self):
        return self.caption

class Comments(models.Model):

    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
        

