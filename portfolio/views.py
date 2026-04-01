from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Skill, Experience, Contact


def home(request):
    projects = Project.objects.filter(is_featured=True)[:6]
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    skills_by_category = {}
    for skill in skills:
        key = skill.category
        if key not in skills_by_category:
            skills_by_category[key] = {
                'display': skill.get_category_display(),
                'skills': []
            }
        skills_by_category[key]['skills'].append(skill)

    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
    }
    return render(request, 'portfolio/index.html', context)


def projects(request):
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'portfolio/projects.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'Message sent successfully!')
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'All fields are required.'})
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'portfolio/contact.html')
