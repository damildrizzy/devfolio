from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Stack(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length = 225)
    owner_id = models.ForeignKey(User, related_name="projects", on_delete = models.CASCADE)
    stack = models.ManyToManyField(Stack)

    @property
    def stack_list():
        return 
        list(self.stack.all())


    def __str__(self):
        return self.name
    


    











