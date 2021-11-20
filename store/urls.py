from django.urls import path
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .views import category_view
from .models import Product

app_name = "store"

urlpatterns = [
    path('', TemplateView.as_view(template_name="store/index.html"), name="index"),
    path('category/<str:name>', category_view, name="category"),
    # path('filter/', filter_view, name="filter"),
    path('product/<int:pk>', DetailView.as_view(model=Product), name="product-detail")
]