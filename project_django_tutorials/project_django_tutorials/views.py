from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here. 
def home(request):
    return HttpResponse("</br></br></br><h1 style='color:darkgreen;text-align:center'>Welcome To My Home Page. !</h1>")
 
def error_view(request, exception):
    return render(request, 'error_view.html', status=404)
 
# def error_500(request, exception):
#     return render(request, 'templates/error_500.html', status=500)
