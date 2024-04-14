from django.shortcuts import render

# Create your views here.
from .models import Note, Image

def list_notes(request):
    all_notes = Note.objects.all()
    
    return render(request, 'note/note_list.html', {'notes': all_notes})

def list_images(request):
    all_images = Image.objects.all()
    
    return render(request, 'note/note_list.html', {'images': all_images})

def list_both(request):
    all_images = Image.objects.all()
    all_notes = Note.objects.all()
    
    return render(request, 'note/both_list.html', {'images': all_images, 'notes': all_notes})