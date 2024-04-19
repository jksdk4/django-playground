from django.shortcuts import render
# from django.http import Http404
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Notes

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