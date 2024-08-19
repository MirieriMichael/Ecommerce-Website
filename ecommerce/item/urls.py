from django.urls import path
from .views import ItemDetailView

app_name = 'item'

urlpatterns = [
    path('<slug:slug>/', ItemDetailView.as_view(), name='detail'),
]
