from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    subject_code = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    question_types = (
        ('A',   'Sec A'),
        ('B',   'Sec B'),
        ('C',   'Sec C'),
    )
    question_type = models.CharField(max_length=20, choices=question_types)
    marks = models.IntegerField(null=True, blank=True)
    difficult_level = models.TextField()
    added_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.question