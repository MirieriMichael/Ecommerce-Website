from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Communication
from .forms import CommunicationMessageForm


def new_communication(request, slug):
    item = get_object_or_404(Item, slug=slug)
    
    # Redirect if the item belongs to the current user
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    # Check if a communication already exists
    communications = Communication.objects.filter(item=item).filter(created_by=request.user)

    if communications.exists():
        communication = communications.first()  # Use the existing communication
    else:
        # Create a new communication if none exists
        communication = Communication.objects.create(item=item, created_by=request.user)
        # communication.members.add(request.user)
        # communication.members.add(item.created_by)
    
    if request.method == 'POST':
        form = CommunicationMessageForm(request.POST)
        if form.is_valid():
            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user  # Set the created_by field
            communication_message.save()
            return redirect('item:detail', slug=slug)
    else:
        form = CommunicationMessageForm()
    
    return render(request, 'communication/new.html', {'form': form, 'item': item})
