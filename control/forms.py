from django import forms
from .models import RequestDocument, RequestEvent, Status


class RequestDocumentForm(forms.ModelForm):
    class Meta:
        model = RequestDocument
        fields = ['title', 'price', 'date_conclusion', 'date_payment', 'status', 'document']
        labels = {
            'title': 'Назва Заявки',
            'price': 'Ціна [UAH]',
            'date_conclusion': 'Дата складання договору',
            'date_payment': 'Дата оплати',
            'status': 'Статус',
            'document': 'Файл документу'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_conclusion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_payment': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'document': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(RequestDocumentForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = 1  # Встановлення статусу за замовчуванням


class UpdateRequestForm(forms.ModelForm):
    new_price = forms.FloatField(label='Нова ціна [UAH]', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    new_date_conclusion = forms.DateField(label='Нова дата складання договору', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    new_date_payment = forms.DateField(label='Нова дата оплати', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    new_status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Новий статус', required=False, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = RequestEvent
        fields = ['title', 'detail', 'author']
        labels = {
            'author': 'Хто вніс зміну*',
            'title': 'Назва події*',
            'detail': 'Опис події*'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'})
        }
