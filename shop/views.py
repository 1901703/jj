from django.shortcuts import render, get_object_or_404
from .models import *

def item_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category': current_category, 'categories':categories, 'items': items})

def item_detail(request, id, item_slug=None):
    item = get_object_or_404(Item, id=id, slug=item_slug)
    return render(request, 'shop/detail.html', {'item': item})

def index(request):
    return render(request, 'shop/index.html')