from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Create_Task


# Create your views here.
# def home(request):
#     return HttpResponse("Hello")

def addTask(request):
    tasks = request.POST['task']
    Create_Task.objects.create(task=tasks)
    # Create_Task.save( )
    return redirect('/todo')


def mark_as_done(request, pk):
    task = get_object_or_404(Create_Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('/todo')


def mark_as_undone(request, pk):
    task = get_object_or_404(Create_Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('/todo')


def edit_task(request, pk):
    get_task = get_object_or_404(Create_Task, pk=pk)
    if request.method == "POST":
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('/todo')
    else:
        context = {
            'get_task': get_task
        }
    return render(request, 'edit.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Create_Task, pk=pk)
    task.delete()
    return redirect('/todo')
