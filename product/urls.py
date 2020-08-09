from django.urls import path

from . import views

urlpatterns = [
    path('basic_product/', views.BasicProductView.as_view(), name="basic_product_view"),
    path('crispy_product/', views.CrispyProductView.as_view(), name="crispy_product_view"),
    path('customize_crispy_product/', views.CustomizeCrispyProductView.as_view(), name="customize_crispy_product_view"),
    path('advance_crispy_product/', views.AdvanceCrispyProductView.as_view(), name="advance_crispy_product_view"),
]