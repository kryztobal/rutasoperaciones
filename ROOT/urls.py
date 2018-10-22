
from django.contrib import admin
from django.urls import path
from .views import index
from app.views import ActivasListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ActivasListView.as_view(), name="index")
]
