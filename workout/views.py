from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Training, Category, Exercise


@login_required
def dashboard_page(request):
    """View for Dashboard page: info about recent trainings"""

    trainings = Training.objects.filter(user__id=request.user.id).order_by('-id')
    context = {
        'trainings': trainings,
    }
    return render(request, "home/dashboard_page.html", context)


@login_required
def add_training_page(request):
    """View for new Training add: form for training data input"""

    if request.method == "GET":
        return render(request, 'home/add_training_page.html')

    if request.method == "POST":
        training = {
            "name": request.POST["name"],
            "description": request.POST["description"],
            "user": request.user,
        }
        new_training = Training.objects.create(**training)
        return redirect('training', new_training.pk)


@login_required
def training_page(request, training_pk):
    """View for Training display"""

    context = {
        'training': Training.objects.get(pk=training_pk),
        'exercises': Exercise.objects.filter(training__pk=training_pk).order_by('-updated_at'),
        'categories': Category.objects.all(),
    }
    return render(request, 'home/single_training_page.html', context)


@login_required
def exercise_page(request, training_pk):
    """View for Exercise input"""

    if request.method == "GET":
        Exercise.objects.get(pk=request.GET["exercise_id"]).delete()
        current_training = Training.objects.get(pk=training_pk)
        Category.objects.get(pk=request.GET["category_id"]).training_set.remove(current_training)
        return redirect('training', training_pk)

    if request.method == "POST":
        new_exercise = {
            "name": request.POST["name"],
            "weight": request.POST["weight"],
            "repetitions": request.POST["repetitions"],
            "training": Training.objects.get(pk=training_pk),
            "category": Category.objects.get(name=request.POST["category"])
        }
        Exercise.objects.create(**new_exercise)
        Training.objects.get(pk=training_pk).categories.add(new_exercise["category"])
        return redirect('training', training_pk)


@login_required
def training_edit_page(request, training_pk):
    """View for Training info edition"""

    context = {
        'training': Training.objects.get(pk=training_pk),
        'exercises': Exercise.objects.filter(training__pk=training_pk),
    }

    if request.method == "GET":
        return render(request, "home/training_edit_page.html", context)

    if request.method == "POST":
        training = {
            'name': request.POST['name'],
            'description': request.POST['description'],
        }
        Training.objects.filter(pk=training_pk).update(**training)
        return redirect('training', training_pk)


@login_required
def training_delete_page(request, training_pk):
    """View for Training delete"""

    Training.objects.get(id=training_pk).delete()
    return redirect('dashboard')


@login_required
def training_fix_page(request, training_pk):
    """View for fixing Training results"""

    if request.method == "GET":
        training = Training.objects.get(pk=training_pk)
        training.is_fixed = True
        training.save()
        return redirect('training', training_pk)


@login_required
def training_unfix_page(request, training_pk):
    """View for fixing Training results"""

    if request.method == "GET":
        training = Training.objects.get(pk=training_pk)
        training.is_fixed = False
        training.save()
        return redirect('training', training_pk)
