from django.shortcuts import render,redirect
from.models import *


# Create your views here.

def homepage(request):
     return render(request,'homepage.html')


def study(request):
     error=""
     if request.method == "POST":
          question = request.POST['question']
          answer = request.POST['answer']
          try:
               Studymaterial.objects.create(title=question, content=answer, )
               error = "no"
          except:
               error = "yes"

     material= Studymaterial.objects.all()
     d={'error': error,'material': material,}
     return render(request,'study.html',d)

def professional(request):
     return render(request,'professional.html',)

def search(request):
    if request.method == 'GET':
        search= request.GET['search']
        filtertitle=Studymaterial.objects.filter(title__icontains=search)
        filtercontent = Studymaterial.objects.filter(content__icontains=search)
        filter= filtertitle.union(filtercontent)


    d = {'filter': filter,'search': search}
    return render(request, 'filter.html', d)

def delete(request,pid):
    apply = Studymaterial.objects.get(id=pid)
    apply.delete()
    return redirect(study)