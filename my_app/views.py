from django.shortcuts import render, HttpResponse
from .models import User, Skills, About, Accomplishments

def home(request):
    # form = ContactMeForm
    user = User.objects.get(id=1)
    user_skills = user.skills.all()
    about = About.objects.get(id=1)
    accomplishments = Accomplishments.objects.all()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(f'{name} - {email} - {subject} - {message}')
    context = {
        'user': user,
        'skills': user_skills,
        'info': about,
        'accomplishments': accomplishments,
        'form': form
    }
    return render(request, 'my_app/index.html', context)
