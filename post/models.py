from django.db import models

# Create your models here.


class Account(models.Model):
    user_name = models.CharField(max_length=255)
    date_of_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=25)
    post_creator = models.ForeignKey(Account, related_name='post', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    time_of_create_post = models.TimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
