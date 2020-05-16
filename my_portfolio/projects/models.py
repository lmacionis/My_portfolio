from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="img/")

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

