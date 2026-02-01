from django.shortcuts import render
from myapp.models import item

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def contact(request):
    data=item.objects.all()
    context={'data':data}
    return render(request,'myapp/contact.html',context=context)


def base(request):
    return render(request,'myapp/base.html',)
