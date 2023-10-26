from django.shortcuts import redirect, render
from django.http import HttpResponse
from todo_app.models import Create_Task

# Create your views here. 
def home2(request):
    return HttpResponse("</br></br></br><h1 style='color:darkgreen;text-align:center'>Welcome To My Home Page. !</h1>")
 
def error_view(request, exception):
    return render(request, 'error_view.html', status=404)

def todo(request):
    # Get all tasks that are not completed
    tasks = Create_Task.objects.filter(is_completed=False).order_by('updated_at')
    # Get all tasks that are completed
    done_tasks = Create_Task.objects.filter(is_completed=True)
    # Render the home page with the tasks
    return render(request, 'home.html', context={'tasks': tasks, 'done_tasks': done_tasks})