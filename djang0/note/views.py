from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q

# @login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes':notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'note/note_detail.html', {'note': note})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            note = form.save(commit=False)
            # note.author = request.user
            note.save()
            return redirect('note:note_list')
    else:
        form = NoteForm()
    return render(request, 'note/create_note.html', {'form': form})

# def login(request):