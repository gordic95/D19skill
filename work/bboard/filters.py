from django_filters import FilterSet
from .models import *

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'title': ['icontains'],
            # поиск по описанию
            # 'content': ['icontains'],
            # поиск по дате
            # 'created_at': ['icontains'],
            # # поиск по автору
            # 'author': ['exact'],
            # поиск по категории
            'type': ['exact'],
            # поиск по цене
            # 'price': ['lt']    # 'lt',   цена должна быть меньше или равна указанной,  'gt',   цена должна быть больше или равна указанной
        }

# В Meta классе мы должны указать Django модель,# в которой будем фильтровать записи.
# В fields мы описываем по каким полям модели # будет производиться фильтрация.