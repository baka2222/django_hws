from django.urls import path
from . import views

urlpatterns = [
    path('men_clothes', views.MenView.as_view(), name='men_clothes'),
    path('women_clothes', views.WomenView.as_view(), name='women_clothes'),
    path('old_men_clothes', views.OldMenView.as_view(), name='old_men_clothes'),
    path('children_clothes', views.ChildrenView.as_view(), name='children_clothes')
]