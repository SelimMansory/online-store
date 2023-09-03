from django import forms
from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price',)

    def clean(self):
        cleaned_date = super().clean()
        name = cleaned_date['name']
        description = cleaned_date['description']
        if set(self.forbidden_words) & set(description.lower().split()) or set(self.forbidden_words) & set(
                name.lower().split()):
            raise forms.ValidationError('Используется запрещенное слово')

        return cleaned_date


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'