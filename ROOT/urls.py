
from django.contrib import admin
from django.urls import path
from .views import index
from app.views import DespachosListView, write_pdf_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DespachosListView.as_view(), name="index"),
    path('mi_pdf', write_pdf_view, name="mi_pdf"),
]