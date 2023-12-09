from django.db import models

""""форма основных меню"""


class Menu(models.Model):
    name = models.CharField('Название основного меню', max_length=100, unique=True)
    description = models.TextField('Описание основного меню', max_length=200, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Основное меню'
        verbose_name_plural = 'Основные меню'

    def __str__(self):
        return self.name


""""форма подменю"""


class MenuItem(models.Model):
    name = models.CharField('Название дочернего меню', max_length=100, unique=True)
    description = models.TextField('Описание дочернего меню', max_length=200, blank=True)
    url = models.CharField(
        verbose_name='Ссылка на другой сайт',
        help_text='При клике на пункт меню кидает на сайт',
        max_length=200, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Дочернее меню'
        verbose_name_plural = 'Дочерние меню'

    def __str__(self):
        return self.name
