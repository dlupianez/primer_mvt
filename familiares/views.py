from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares

# Create your views here.
def create_relatives(request):
    """Function for creating relatives"""
    new_relative1=Familiares.objects.create(name='Miguel',is_lotr_fan=True, age=71)
    new_relative2=Familiares.objects.create(name='Cristina',is_lotr_fan=True, age=71)
    new_relative3=Familiares.objects.create(name='Gisela',is_lotr_fan=True, age=44)
    new_relative4=Familiares.objects.create(name='Cristian',is_lotr_fan=True, age=41) 
    new_relative5=Familiares.objects.create(name='Daiana',is_lotr_fan=True, age=30)
    print(new_relative1,new_relative2, new_relative3, new_relative4, new_relative5)
    return HttpResponse('New relatives created')

def list_relatives(request):
    """Function for listing relatives"""
    all_relatives = Familiares.objects.all()
    print(all_relatives)
    context = {
        'familiares': all_relatives,
    }
    return render(request, 'list_relatives.html',context=context)
