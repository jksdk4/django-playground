from django.shortcuts import render
# from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    # points to this file I created instead of auto assuming it would be 'notes/notes_confirm_delete.html'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm  # allows more powerful validation than having fields here.


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    # overrides the get_queryset default method.
    # https://ccbv.co.uk/projects/Django/5.0/django.views.generic.list/ListView/
    def get_queryset(self):
        return self.request.user.notes.all()

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
