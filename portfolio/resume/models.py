from django.db import models


class skill(models.Model):
    name=models.CharField(max_length=100)
    point=models.IntegerField()
    def __str__(self):
        return self.name

class experience(models.Model):
    position=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    start_work=models.CharField(max_length=100)
    end_work=models.CharField(max_length=100)
    description=models.TextField()
    url=models.URLField(blank=True)
    def __str__(self):
        return self.start_work+'-'+self.end_work

class education(models.Model):
    location=models.CharField(max_length=100)
    start_year=models.CharField(max_length=100)
    end_year=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    def __str__(self):
        return self.start_year+'-'+self.end_year

class license(models.Model):
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    url=models.URLField(blank=True)
    def __str__(self):
        return self.name
