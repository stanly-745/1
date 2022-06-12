from django import forms
from django.forms import ModelForm
from .models import *

# customer form
class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

# worker form
class WorkerForm(ModelForm):
    class Meta:
        model=Worker
        fields='__all__'

# product form
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

# stock form
class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields='__all__'

# order form
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

# bill form
class billform(forms.ModelForm):
	class Meta:
		model=Bill 
		fields=['customer_name']


class billproductform(forms.ModelForm):
	class Meta:
		model=bill_product
		fields=['billprod','quantity']
