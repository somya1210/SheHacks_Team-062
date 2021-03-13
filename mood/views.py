from django.shortcuts import render, redirect


def index(request):
    
    return render(request, 'mood/index.html', {})


def article(request):
    return render(request, 'mood/article.html', {})


def doctor(request):
    return render(request, 'quiz/doctor.html', {})
