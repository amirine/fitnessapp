from django.db import models


class Training(models.Model):
    day_number = models.IntegerField()
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    is_active_day = models.BooleanField()
    categories = models.ManyToManyField('Category')
    equipment = models.ManyToManyField('Equipment')
    video = models.OneToOneField('Video', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
        ordering = ['day_number']

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=24)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    name = models.CharField(max_length=24)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    is_added_to_favourites = models.BooleanField()
    file = models.FileField(upload_to='workout/videos', null=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return f'{self.name}'
