from django.shortcuts import render,redirect

def index(request):
    if request.method=="POST":
        description=request.GET.get('description')
        amount=request.GET.get('amount')

        if description is None:
           return redirect('/')
    
    
    
    return render(request, 'index.html')
