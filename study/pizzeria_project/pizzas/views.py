from django.shortcuts import render
from .models import Pizza,Topping
def index(request):
    pizzas = Pizza.objects.all()
    toppings = Topping.objects.all() 
    context={'pizzas':pizzas,'topping'
             :toppings}
    return render(request,
        'pizzas/index.html',context)
# Create your views here.
