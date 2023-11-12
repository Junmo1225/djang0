from django.shortcuts import render, get_object_or_404, redirect
# from .models import Note
# from.forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q

# @login_required
def note_list(request):
    return render(request, 'note/note_list.html')