from django.shortcuts import render
# from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

# Create your views here.
from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm      # allows more powerful validation than having fields here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

    ''' 
    it's 'note' and not 'notes' because it's passing in a single
    'note' into the notes_detail template
    '''
    
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except:
#         raise Http404("Note doesn't exist.")
#     return render(request, 'notes/notes_detail.html', {'note': note})