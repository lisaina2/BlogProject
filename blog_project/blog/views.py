from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse("list")

def post_detail(request, id):
    return HttpResponse("detail "+str(id))

