from django.views import generic
from .models import Cloth


class MenView(generic.ListView):
    template_name = 'clothes/men.html'
    model = Cloth
    context_object_name = 'clothes'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='#одежда для мужчин').order_by('-id')


class WomenView(generic.ListView):
    template_name = 'clothes/women.html'
    model = Cloth
    context_object_name = 'clothes'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='#одежда для женщин').order_by('-id')


class OldMenView(generic.ListView):
    template_name = 'clothes/old_men.html'
    model = Cloth
    context_object_name = 'clothes'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='#одежда для пенсионеров').order_by('-id')


class ChildrenView(generic.ListView):
    template_name = 'clothes/children.html'
    model = Cloth
    context_object_name = 'clothes'

    def get_queryset(self):
        return Cloth.objects.filter(tags__name='#одежда для детей').order_by('-id')