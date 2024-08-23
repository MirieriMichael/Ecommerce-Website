# from django.shortcuts import render, get_object_or_404
# from .models import Item

# def detail(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     return render(request, 'item/detail.html', {'item': item})
from django.views.generic import DetailView
from .models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewItemForm
class ItemDetailView(DetailView):
    model = Item
    template_name = 'detail.html'  # Correct this to reflect the correct path
    context_object_name = 'item'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()  # Get the current item
        # Add related items to the context
        context['related_items'] = Item.objects.filter(
            category=item.category,
            is_sold=False
        ).exclude(slug=item.slug)
        return context
@login_required
def new_Item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES, request=request)  # Pass 'request' here
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail', slug=form.instance.slug)  # Assuming you have a slug
    else:
        form = NewItemForm(request=request)  # Pass 'request' here for the GET request
    
    return render(request, 'form.html', {
        'form': form,
        'title': 'Add Item'
    })
@login_required
def delete(request,slug):
    item=get_object_or_404(Item,slug=slug,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')