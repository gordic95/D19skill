from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)  # ограничение на длину описания

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'type', 'price')

        def clean(self):
            cleaned_data = super().clean()  # вызываем метод родителя
            content = cleaned_data.get("content")   # получаем значение для поля content
            # if content is not None and len(content) < 10:    # если описание меньше 10 символов, то ошибка!
            #     raise ValidationError({    # ошибка валидации
            #         "content": "Описание не может быть меньше, чем 10 символов!"})

            title = cleaned_data.get("title")    # получаем значение для поля title
            if title == content:  # если название и описание равны, то ошибка!
                raise ValidationError({       # ошибка валидации
                    "title": "Название не должно быть идентичным описанию"})
            return cleaned_data
