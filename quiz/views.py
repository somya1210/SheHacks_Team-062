from django.shortcuts import render
from .models import *

# Create your views here.
def quiz(request):
    questions = Quiz.objects.all()
    answer = "ans"
    context = {'questions': questions, 'answer':answer}
    # if request.method =="POST":
    #     res = 0
    #     for i in range(10):
    #         one = request.POST.get("c"+ str(i+1), 'off')
            
    #         if one=="on":
    #             res+=1
    #         elif two=="on":
    #             res+=4
    #         elif three=="on":
    #             res+=7
    #         else:
    #             res+=9
            
        
        # return render(request, 'quiz/result.html',context)
   
    return render(request, 'quiz/quiz.html', context)

def result(request):
    # if request.method =="POST":
    #     result = request.POST.get("result")
    #     context = {'result':result}
    #     return render(request, 'quiz/result.html',context)
    
    # questions = Quiz.objects.all()
    # context = {'questions': questions}
   
    return render(request, 'quiz/result.html', {})
