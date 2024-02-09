from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('signin/', views.SignInView.as_view(), name='login'),
    path('signout/', views.SignOutView.as_view(), name='logout'),
    path('accounts_list/', views.AccuntListView.as_view(), name='accounts_list')
]