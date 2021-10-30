from django.http import HttpResponse
from django.shortcuts import render
from .models import Training, Category


def trainings_page_view(request):
    """View for Training page: list of trainings with description"""
    context = {
        'trainings': Training.objects.all(),
    }
    print(context['trainings'].first().video.file)
    return render(request, 'workout/trainings_page.html', context)
