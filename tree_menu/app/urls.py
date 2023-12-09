from django.urls import path

from .views import show_menu, main

urlpatterns = [
    path('', main, name='main_menu'),
    path('<path:path>/', show_menu, name='show_menu')
]
