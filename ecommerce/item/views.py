# from django.shortcuts import render, get_object_or_404
# from .models import Item

# def detail(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     return render(request, 'item/detail.html', {'item': item})
from django.views.generic import DetailView
from .models import Item

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