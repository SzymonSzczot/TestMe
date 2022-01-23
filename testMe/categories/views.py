from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader
from trials.models import Test

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@login_required
def category(request, category_name):
    context = {}
    context['name'] = category_name
    context['tests'] = Test.objects.filter(category=category_name)
    return render(request, 'category.html', context)