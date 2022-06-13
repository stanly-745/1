from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
# -----------LOGIN---------------#
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user)
                return redirect('login')

        context={'form':form}
        return render(request,'app/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')

            else:
                messages.info(request,'Username OR Password is incorrect')

        context={}
        return render(request,'app/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')
# -----------LOGIN-------------#
# home

@login_required(login_url='login')
def home(request):
    no_order=Order.objects.count()
    pending_order=Order.objects.filter(status='Not-Delivered').count()
    customer=Customer.objects.all()
    worker=Worker.objects.all()
    product=Product.objects.all().count()
    stock=Stock.objects.filter(quantity=0).count()
    context={'product':product,'customer':customer,'worker':worker,'pending_order':pending_order,'no_order':no_order,'stock':stock}
    return render(request,'app/home.html',context)

# customer page
@login_required(login_url='login')
def customer(request,pk):
    customers=Customer.objects.get(id=pk)
    context={'customer':customers}
    return render(request,'app/customer.html',context)

# worker page
@login_required(login_url='login')
def worker(request,pk):
    workers=Worker.objects.get(id=pk)
    context={'worker':workers}
    return render(request,'app/worker.html',context)
# -------------------------------------------------------
# order page
@login_required(login_url='login')
def order(request):
    orders=Order.objects.filter(status='Not-Delivered').all()
    context={'orders':orders}
    return render(request,'app/order.html',context)

# order history
@login_required(login_url='login')
def order_history(request):
    orders=Order.objects.all()
    context={'orders':orders}
    return render(request,'app/order_history.html',context)

# update order
@login_required(login_url='login')
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
@login_required(login_url='login')
def stock(request):
    stock=Stock.objects.all()
    stocks=Stock.objects.filter(quantity=0).all()
    context={'stock':stock,'stocks':stocks}
    return render(request,'app/stock.html',context)

# product page
@login_required(login_url='login')
def product(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'app/product.html',context)

# update stock
@login_required(login_url='login')
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
@login_required(login_url='login')
def customerform(request):
    form=CustomerForm()
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcus')
    context={'form':form}
    return render(request,'app/customer_form.html',context)

# worker form
@login_required(login_url='login')
def workerform(request):
    form=WorkerForm()
    if request.method=='POST':
        print(request.POST)
        form=WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addwor')
    context={'form':form}
    return render(request,'app/worker_form.html',context)

# product form
@login_required(login_url='login')
def productform(request):
    form=ProductForm()
    if request.method=='POST':
        print(request.POST)
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addpro')
    context={'form':form}
    return render(request,'app/product_form.html',context)

# stock form
@login_required(login_url='login')
def stockform(request):
    form=StockForm()
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsto')
    context={'form':form}
    return render(request,'app/stock_form.html',context)

# order form
@login_required(login_url='login')
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


# ----------bill----------------#
@login_required(login_url='login')
def calcsum(request,pk):
    bill_obj=Bill.objects.get(bill_num=pk)
    products_set=bill_product.objects.filter(bill_item=bill_obj)
    total=5
    
    for product in products_set:
        price=product.billprod.price
        qty=product.quantity
        item_sum=price*qty
        total=total+item_sum
    bill_obj.total_sum=total
    bill_obj.save()
    return redirect('bill-detail',pk=bill_obj.bill_num)

@login_required(login_url='login')
def billgeneration(request):
    bill_obj=billform(request.POST)
    if bill_obj.is_valid():
       bills=bill_obj.save()
       return redirect('calc-sum',pk=bills.bill_num)
    return render(request,'app/billadd_form.html',{'form':billform})


@login_required(login_url='login')
def billdetail(request,pk):
    bill_obj=Bill.objects.get(bill_num=pk)
    bill_prds=bill_product.objects.filter(bill_item=bill_obj)
    context={
        'bill':bill_obj,
        'products':bill_prds
    }
    return render(request,'app/bill_detail.html',context)

@login_required(login_url='login')
def bill_prod_add(request,pk):
    billing_form=billproductform(request.POST)
    bill_obj=Bill.objects.get(bill_num=pk)
    if billing_form.is_valid():
        billform_obj=billing_form.save(commit=False)
        product_obj=billform_obj.billprod
        qty=billform_obj.quantity
        try :
            bill_info=bill_product.objects.get(bill_item=bill_obj,billprod=product_obj)
            bill_info.quantity=qty
            bill_info.save()
        except bill_product.DoesNotExist:
            bills=billing_form.save(commit=False)
            bills.bill_item=bill_obj
            bills.save()

        return redirect('calc-sum',pk=bill_obj.bill_num)
    return render(request,'app/billadd_form.html',{'form':billing_form})

# Expence view
@login_required(login_url='login')
def expense(request):
    expenses=Expense.objects.all()
    return render(request,'app/expense.html',{'expense':expenses})

@login_required(login_url='login')
def expenseform(request):
    form=ExpenseForm()
    if request.method=='POST':
        print(request.POST)
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense')
    context={'form':form}
    return render(request,'app/expense_form.html',context)

@login_required(login_url='login')
def income(request):
    income=Income.objects.all()
    return render(request,'app/income.html',{"income":income})

@login_required(login_url='login')
def incomeform(request):
    form=IncomeForm()
    if request.method=='POST':
        print(request.POST)
        form=IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income')
    context={'form':form}
    return render(request,'app/income_form.html',context)