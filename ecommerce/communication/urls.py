from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('new/<slug:slug>', views.new_communication, name='new'),  # Ensure the slug is included in the pattern
]
