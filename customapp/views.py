from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User was created successfully')
        else:
            return HttpResponse('User was not Created,Ther was an error.')
    else:
        form = CustomUserForm()
        
    return render(request, 'customapp/home.html', {'form': form})