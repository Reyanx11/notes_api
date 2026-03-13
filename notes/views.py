
from .models import Notes
from .serializer import NotesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

@api_view(['GET','POST'])
def note_list(request):
    if request.method == 'GET':

        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = NotesSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def note_details(request, pk):

    try:
        note = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        raise Http404
    
    if request.method == 'GET':
        serializer = NotesSerializer(note)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        note.delete()
        return Response(status = 204)
        