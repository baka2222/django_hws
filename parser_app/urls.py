from django.urls import path
from .views import ParserView, HousesListView

urlpatterns = [
    path('parser/', ParserView.as_view(), name='parser'),
    path('houses/', HousesListView.as_view(), name='house.kg')
]