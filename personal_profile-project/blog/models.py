from django.db import models

class Test(models.Model):
    title = models.CharField(max_length = 100)
    discription = models.CharField(max_length = 250)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    discription = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
