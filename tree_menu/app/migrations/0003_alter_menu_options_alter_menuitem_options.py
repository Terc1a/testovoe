# Generated by Django 4.2.1 on 2023-12-09 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_menuitem_options_alter_menu_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['id'], 'verbose_name': 'Основное меню', 'verbose_name_plural': 'Основные меню'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['id'], 'verbose_name': 'Дочернее меню', 'verbose_name_plural': 'Дочерние меню'},
        ),
    ]
