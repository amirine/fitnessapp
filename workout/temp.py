from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Training, Category, Exercise, Equipment


@login_required
def home_page(request):
    """View for Home page: user greeting with some information"""

    trainings = Training.objects.filter(user__id=request.user.id).order_by('-id')[:6]
    context = {
        'trainings': trainings,
    }
    return render(request, 'home/dashboard_page.html')


@login_required
def dashboard_page(request):
    """View for Dashboard page: info about recent trainings"""

    trainings = Training.objects.filter(user__id=request.user.id).order_by('-id')[:6]
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

# @login_required
# def test_add(request):
#
#     if request.method == "GET":
#         return render(request, 'home/add_training_page.html')
#
#     if request.method == "POST":
#         training = {
#             "name": request.POST["name"],
#             "description": request.POST["description"],
#             "user": request.user,
#         }
#         new_training = Training.objects.create(**training)
#         return redirect('test_training', new_training.pk)



@login_required
def training_page(request, training_pk):
    """View for Training display"""

    # if request.method == "GET":
    context = {
        'training': Training.objects.get(pk=training_pk),
        'exercises': Exercise.objects.filter(training__pk=training_pk).order_by('-updated_at'),
    }
    return render(request, "workout/training_page.html", context)


@login_required
def all_trainings_page(request):
    """View for all trainings list"""

    all_trainings = Training.objects.filter(user__id=request.user.id).order_by('-id')
    # page = request.GET.get('page', 1)
    # paginator = Paginator(workout_list, 12)
    # try:
    #     workouts = paginator.page(page)
    # except PageNotAnInteger:
    #     workouts = paginator.page(1)
    # except EmptyPage:
    #     workouts = paginator.page(paginator.num_pages)
    context = {
        'trainings': all_trainings,
    }
    return render(request, "workout/all_trainings_page.html", context)


@login_required
def exercise_page(request, training_pk):
    """View for Exercise input"""

    if request.method == "GET":
        Exercise.objects.get(pk=request.GET["exercise_id"]).delete()
        return redirect('training', training_pk)

    if request.method == "POST":
        new_exercise = {
            "name": request.POST["name"],
            "weight": request.POST["weight"],
            "repetitions": request.POST["repetitions"],
            "training": Training.objects.get(pk=training_pk),
        }
        Exercise.objects.create(**new_exercise)
        return redirect('training', training_pk)


@login_required
def training_edit_page(request, training_pk):
    """View for Training info edition"""

    context = {
        'training': Training.objects.get(pk=training_pk),
        'exercises': Exercise.objects.filter(training__pk=training_pk),
    }

    if request.method == "GET":
        return render(request, "workout/training_edit_page.html", context)

    if request.method == "POST":
        training = {
            'name': request.POST['name'],
            'description': request.POST['description'],
        }
        Training.objects.filter(pk=training_pk).update(**training)
        return redirect('training', training_pk)


@login_required
def training_delete_page(request, pk):
    """View for Training delete"""

    Training.objects.get(id=pk).delete()
    return redirect('dashboard')


@login_required
def training_fix_page(request, pk):
    """View for fixing Training results"""

    if request.method == "GET":
        return redirect('training', pk)

    if request.method == "POST":
        training = Training.objects.get(id=pk)
        training.is_fixed = True
        training.save()
        return redirect('training', pk)

# @method_decorator(login_required, name='dispatch')
# class TrainingsView(ListView):
#     """View for Training page: list of trainings with description"""
#     model = Training
#     template_name = 'workout/trainings_page.html'
#     context_object_name = 'trainings'

# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title'] = 'Trainings Page'
#     context['selected'] = 0
#     return context

# def get_queryset(self):
#     return Training.objects.filter(pk=1)

# class SingleTrainingView(DetailView):
#     model = Training
#     template_name = 'workout/single_training_page.html'
#     pk_url_kwarg = 'training_pk'
#     context_object_name = 'training'

@login_required
def test_add(request):

    if request.method == "GET":
        return render(request, 'home/add_training_page.html')

    if request.method == "POST":
        training = {
            "name": request.POST["name"],
            "description": request.POST["description"],
            "user": request.user,
        }
        new_training = Training.objects.create(**training)
        return redirect('test_training', new_training.pk)


# @login_required
# def test_training(request):
#     return render(request, 'home/training_page.html')

@login_required
def test_training_all(request):
    return render(request, 'home/all_trainings_page.html')

@login_required
def test_training(request, training_pk):
    """View for Training display"""

    # if request.method == "GET":
    context = {
        'training': Training.objects.get(pk=training_pk),
        'exercises': Exercise.objects.filter(training__pk=training_pk).order_by('-updated_at'),
        'categories': Category.objects.all(),
    }
    return render(request, 'home/training_page.html', context)

@login_required
def test_exercise_page(request, training_pk):
    """View for Exercise input"""

    if request.method == "GET":
        Exercise.objects.get(pk=request.GET["exercise_id"]).delete()
        Training.objects.get(pk=training_pk).categories.get(pk=request.GET["category_id"]).delete()

        return redirect('test_training', training_pk)

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
        return redirect('test_training', training_pk)

@login_required
def test_training_edit_page(request, training_pk):
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
        return redirect('test_training', training_pk)

@login_required
def test_training_delete_page(request, training_pk):
    """View for Training delete"""

    Training.objects.get(id=training_pk).delete()
    return redirect('dashboard')

@login_required
def test_training_fix_page(request, training_pk):
    """View for fixing Training results"""

    # if request.method == "GET":
    #     return redirect('test_training', training_pk)

    if request.method == "GET":
        training = Training.objects.get(id=training_pk)
        training.is_fixed = True
        training.save()
        return redirect('test_training', training_pk)
