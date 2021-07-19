from django.shortcuts import render
from.models import *
import pyttsx3
from django.contrib import messages

# Create your views here.

def homepage(request):
     return render(request,'homepage.html')



def resumeread(request):
     if request.method == "POST":
          value = request.POST['honey']
          engine = pyttsx3.init()
          engine.say(value)
          engine.runAndWait()
     return render(request,'homepage.html')





