from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_default_user():
    return get_user_model().objects.first().id 
class Communication(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)  # Ensure this field exists
    subject = models.CharField(max_length=255,default='No subject',null=True)  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        # 
        pass
class CommunicationMessage(models.Model):
    communication=models.ForeignKey(Communication,related_name='messages',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='created_messages',on_delete=models.CASCADE,)