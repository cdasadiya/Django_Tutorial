from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

pages_name ={
    'diwali':'Celebration of Joy , Prosperties and Healthy life !',
    'holy': 'Celebration of Colours With Joy !',
    'navratri':'Celebration of Graba & Dandiya Ras !',
}
def dynamic_views(request,topics):
    try:
        return HttpResponse("</br></br></br><h1 style='color:magenta;text-align:center'>%s</h1>" % pages_name[topics])
    except:
        return HttpResponseNotFound("404 found")