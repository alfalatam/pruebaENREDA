from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import note, User


def create_note(request):
    notes = note.objects.all()
    users = User.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        Type = request.POST.get('Type')
        Note = request.POST.get('Note')
        task = request.POST.get('task')
        Date = request.POST.get('Date')
        EndDate = request.POST.get('EndDate')
        Adjunto = request.POST.get('Adjunto')
        tags = request.POST.get('tags')
        user = request.POST.get('user')

        response_data['Type'] = Type
        response_data['Note'] = Note
        response_data['task'] = task
        response_data['Date'] = Date
        response_data['EndDate'] = EndDate
        response_data['tags'] = tags
        response_data['user'] = user

        note.objects.create(
            Type=Type,
            Note=Note,
            task=task,
            EndDate=EndDate,
            Date=Date,
            Adjunto=Adjunto,
            tags=tags,
            user=user,
        )
        return JsonResponse(response_data)

    return render(request, 'inicio.html', {'notes': notes, 'users': users})
