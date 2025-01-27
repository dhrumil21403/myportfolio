from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

# Create your views here.
def home(request):
    context={}
    return render(request,"index.html",context)

def download_resume(request):
    # File path to your resume in the media folder
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdhrumilresume.pdf')
      # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary mode and create a response
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='pdhrumilresume.pdf')
        return response
    else:
        # Return a 404 response if the file is not found
        from django.http import Http404
        raise Http404("The requested file was not found.")
    
def download_pizza(request):
    # File path to your resume in the media folder
    file_path = os.path.join(settings.MEDIA_ROOT, 'Pizza Sales Analysis 2015 report.pdf')
      # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary mode and create a response
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Pizza Sales Analysis 2015 report.pdf')
        return response
    else:
        # Return a 404 response if the file is not found
        from django.http import Http404
        raise Http404("The requested file was not found.")
    
def download_helpinghand(request):
    # File path to your resume in the media folder
    file_path = os.path.join(settings.MEDIA_ROOT, 'Helping_hand - Copyfinalforthesis.pdf')
      # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary mode and create a response
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Helping_hand - Copyfinalforthesis.pdf')
        return response
    else:
        # Return a 404 response if the file is not found
        from django.http import Http404
        raise Http404("The requested file was not found.")
    
def download_enoticeboard(request):
    # File path to your resume in the media folder
    file_path = os.path.join(settings.MEDIA_ROOT, 'dhrumilpp.pptx')
      # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary mode and create a response
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='dhrumilpp.pptx')
        return response
    else:
        # Return a 404 response if the file is not found
        from django.http import Http404
        raise Http404("The requested file was not found.")