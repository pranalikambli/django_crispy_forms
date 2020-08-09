from django.views.generic import CreateView

from .models import Products
from .forms import ProductForm

class BasicProductView(CreateView):
    model = Products
    template_name = 'basic_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/basic_product"

class CrispyProductView(CreateView):
    model = Products
    template_name = 'crispy_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/crispy_product"

class CustomizeCrispyProductView(CreateView):
    model = Products
    template_name = 'customize_crispy_product_view.html'
    fields = ['name', 'price', 'category', 'description']
    success_url = "/customize_crispy_product"

class AdvanceCrispyProductView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'advance_crispy_product_view.html'
    success_url = "/advance_crispy_product"