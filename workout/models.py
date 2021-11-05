from django.contrib.auth.models import User
from django.db import models


class Training(models.Model):
    """Model for training"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    is_fixed = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category')
    equipment = models.ManyToManyField('Equipment')
    duration = models.IntegerField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name}'


class Exercise(models.Model):
    """Model for Exercises included in Training"""
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=200)
    repetitions = models.DecimalField(max_digits=1000)
    training = models.ForeignKey('Training', default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Exercises'
        verbose_name_plural = 'Exercise'

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    """Model for Training category"""
    name = models.CharField(max_length=24)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    """Model for Training equipment"""
    name = models.CharField(max_length=24)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return f'{self.name}'
