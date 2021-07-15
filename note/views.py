from django.shortcuts import render
from .models import Note, NoteForm


def index(request):
    notes = Note.objects.all()
    note_form = NoteForm()
    context = {'notes' : notes, 'note_form' : note_form}
    return render(request,'index.html', context)

def base(request):
    context = { }
    return render(request,'base.html')
