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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class DeleteProfileForm(forms.Form):
    pass
