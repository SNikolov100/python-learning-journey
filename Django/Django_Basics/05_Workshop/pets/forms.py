from django import forms

from common.mixins import DisableMixin
from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_pet_photo']
        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_pet_photo': 'Link to image'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_pet_photo': forms.URLInput(attrs={'placeholder': 'Link to image'})
        }

class PetCreateForm(PetForm):
    ...


class PetEditForm(PetForm):
    ...

class PetDeleteForm(DisableMixin, PetForm):
    ...
