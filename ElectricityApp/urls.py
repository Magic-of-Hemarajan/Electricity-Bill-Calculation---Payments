from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.Login_view, name='login'),
    path('home/', views.home, name='home'),
    path('home/Duecalculation/', views.Due_calculation, name='Due_calculation'),
    path('payments/', views.payments_view, name='payments'),
    path('generate/', views.generate, name='generate'),
    path('logout/', views.logout_view, name='logout')
]
