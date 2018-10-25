
from django.contrib import admin
from django.urls import path
from .views import index
from app.views import DespachosListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DespachosListView.as_view(), name="index")
]
