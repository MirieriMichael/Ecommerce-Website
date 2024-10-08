from django.urls import path
from .views import ItemDetailView
from .import views
app_name = 'item'

urlpatterns = [
    path('',views.items,name='items',),
    path('new_Item/',views.new_Item,name='new_Item'),
    path('<slug:slug>/', ItemDetailView.as_view(), name='detail'),
       path('<slug:slug>/delete/',views.delete, name='delete'),
        path('<slug:slug>/edit/',views.edit, name='edit')
]
