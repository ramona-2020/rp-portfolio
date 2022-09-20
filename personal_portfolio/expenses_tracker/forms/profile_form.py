import os

from django import forms

from personal_portfolio.expenses_tracker.models import Profile
from personal_portfolio.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

            # delete image from filestorage
            if self.instance.image:
                image_path = self.instance.image.path
                os.remove(image_path)
        return self.instance
