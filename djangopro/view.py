# This is created my my Own
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hello django</h1>")

def about(request):
    return HttpResponse('hello This is About Page')
    # hello comment