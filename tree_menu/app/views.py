from django.shortcuts import render

from .models import Menu


def main(request):
    return render(request, 'app/index.html', {'menus': Menu.objects.all()})


def show_menu(request, path):
    split_path = path.split('/')
    return render(request, 'app/index.html', {'menu_name': split_path[0], 'menu_item': split_path[-1]})
