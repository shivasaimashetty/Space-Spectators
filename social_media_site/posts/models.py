from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.utils import timezone
# Create your models here.\
from django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete='CASCADE')
    created_date=models.DateTimeField(auto_now=True)
    message=models.TextField()
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group,related_name='posts',on_delete=models.CASCADE,null=True,blank=True)
    photo=models.ImageField(upload_to='posts/images',blank=True,null=True)


    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering=['-created_date']
        unique_together=['user','message']

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete='CASCADE')
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
