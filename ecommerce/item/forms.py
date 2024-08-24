from django import forms
from django.contrib.auth.decorators import login_required
from .models import Item
INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Pop 'request' from kwargs
        super(NewItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets={
            'category':forms.Select(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
            'name':forms.TextInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
            'description':forms.Textarea(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
              'price':forms.TextInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
              'image':forms.FileInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            })
        }
        
class EditItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Pop 'request' from kwargs
        super(EditItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image','is_sold')
        widgets={
            'category':forms.Select(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
            'name':forms.TextInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
            'description':forms.Textarea(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
              'price':forms.TextInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            }),
              'image':forms.FileInput(attrs={
            'class':'w-full py-4 px-6 rounded-xl border'  
            })
        }
        