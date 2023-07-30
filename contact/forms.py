from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.http import Http404
from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    frist_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Escreva aqui',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuario',
    )

    class Meta:
        model = models.Contact
        fields = (
            'frist_name', 'last_name', 'phone',
        )
        # widgets = {
        #     'frist_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }
        def clean(self):
            cleaned_data = self.cleaned_data
            frist_name = cleaned_data.get('frist_name')
            last_name = cleaned_data.get('last_name')

            if frist_name == last_name:

                msg = ValidationError(
                    'Primeiro nome nao pode ser igual o segundo',
                    code='invalid'
                )
                self.add_error('frist_name', msg)
                self.add_error('last_name', msg)
            return super().clean()



    def clean_frist_name(self):
        frist_name = self.cleaned_data.get('frist_name')

        if frist_name == 'ABC':
            self.add_error('frist_name')
            ValidationError(
                'Veio do add_error',
                code='invalid'
            )
        return frist_name




