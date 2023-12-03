from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
# from.forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q

# @login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes':notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/note_detail.html', {'note': note})
