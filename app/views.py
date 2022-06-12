from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    no_order=Order.objects.count()
    pending_order=Order.objects.filter(status='Not-Delivered').count()
    customer=Customer.objects.all()
    worker=Worker.objects.all()
    stock=Stock.objects.filter(quantity=0).count()
    context={'customer':customer,'worker':worker,'pending_order':pending_order,'no_order':no_order,'stock':stock}
    return render(request,'app/home.html',context)

# customer page
def customer(request,pk):
    customers=Customer.objects.get(id=pk)
    context={'customer':customers}
    return render(request,'app/customer.html',context)

# worker page
def worker(request,pk):
    workers=Worker.objects.get(id=pk)
    context={'worker':workers}
    return render(request,'app/worker.html',context)
# -------------------------------------------------------
# order page
def order(request):
    orders=Order.objects.filter(status='Not-Delivered').all()
    context={'orders':orders}
    return render(request,'app/order.html',context)

# order history
def order_history(request):
    orders=Order.objects.all()
    context={'orders':orders}
    return render(request,'app/order_history.html',context)

# update order
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('order')
    context={'form':form}
    return render(request,'app/order_form.html',context)

# --------------------------------------------------------

# stock in page
def stock(request):
    stock=Stock.objects.all()
    stocks=Stock.objects.filter(quantity=0).all()
    context={'stock':stock,'stocks':stocks}
    return render(request,'app/stock.html',context)

# update stock
def update_stock(request,pk):
    stock=Stock.objects.get(id=pk)
    form=StockForm(instance=stock)
    if request.method=='POST':
        form=StockForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context={'form':form}
    return render(request,'app/stock_form.html',context)

# customer form
def customerform(request):
    form=CustomerForm()
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/customer_form.html',context)

# worker form
def workerform(request):
    form=WorkerForm()
    if request.method=='POST':
        print(request.POST)
        form=WorkerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/worker_form.html',context)

# product form
def productform(request):
    form=ProductForm()
    if request.method=='POST':
        print(request.POST)
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/product_form.html',context)

# stock form
def stockform(request):
    form=StockForm()
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/stock_form.html',context)

# order form
def orderform(request):
    form=OrderForm()
    if request.method=='POST':
        print(request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addord')
    context={'form':form}
    return render(request,'app/order_form.html',context)