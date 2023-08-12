from django.shortcuts import render , redirect, get_object_or_404
from .forms import  TaskForm # Import the RegistrationForm you created in forms.py
from .models import Task # Import your model


# Create your views here.
def home(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the task to the database
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = TaskForm()

    return render(request, 'home.html', {'form': form, 'tasks': tasks})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after updating

    else:
        form = TaskForm(instance=task)

    return render(request, 'edit.html', {'form': form, 'task': task})
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')