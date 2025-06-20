# api/views.py
from django.http import HttpResponse

def api_home(request):
    return HttpResponse("Hello from the API app!")
