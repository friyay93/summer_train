from django.http.response import HttpResponse
from django.shortcuts import render

# def post_list(request):
#     return HttpResponse("<h1> Helloworld </h1>")

def power_point(request):
    return render(request, 'power_point.html')