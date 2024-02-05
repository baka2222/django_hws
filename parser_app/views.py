from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Houses
from .forms import ParserForm


class ParserView(generic.CreateView):
    template_name = 'parser/parser.html'
    form_class = ParserForm
    context_object_name = 'form'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Исключаем 'instance' из kwargs
        return kwargs
    #Была проблема с неким аргументов 'instance'. Всю ночь решал, потом ChatGPT помог

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser()
            return HttpResponse('Данные взяты')
        else:
            return super(ParserView, self).post(request, *args, **kwargs)


class HousesListView(generic.ListView):
    template_name = 'parser/houses.html'
    model = Houses
    context_object_name = 'houses'

    def get_queryset(self):
        return Houses.objects.all()