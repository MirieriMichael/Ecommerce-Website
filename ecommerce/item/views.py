# from django.shortcuts import render, get_object_or_404
# from .models import Item

# def detail(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     return render(request, 'item/detail.html', {'item': item})
from django.views.generic import DetailView
from .models import Item,Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewItemForm,EditItemForm
from django.db.models import Q
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
@login_required
def edit(request,slug):
    item=get_object_or_404(Item,slug=slug,created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, request=request,instance=item)  # Pass 'request' here
        if form.is_valid():
           form.save()
           return redirect('item:detail', slug=form.instance.slug)  # Assuming you have a slug
    else:
        form = EditItemForm(instance=item)  # Pass 'request' here for the GET request
    
    return render(request, 'form.html', {
        'form': form,
        'title': 'Add Item'
    })
def items(request):
    query = request.GET.get('query', '')
    category_slug = request.GET.get('category', '')  # Get the category slug from the query string
    categories = Category.objects.all()

    print("Category Slug:", category_slug)  # Debugging line
    items = Item.objects.filter(is_sold=False)

    if category_slug:  # Ensure it's not an empty string
        items = items.filter(category__slug=category_slug)  # Filter by the selected category

    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'selected_category_slug': category_slug,  # Pass the selected category slug to the template
    })
