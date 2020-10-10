from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                'username',
                'email',
                ButtonHolder(
                    Submit('submit', 'Salvar', css_class=''),
                    Reset('reset', 'Limpar', css_class='btn-danger')
                )
            )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.layout = Layout(
                'username',
                'email',
                ButtonHolder(
                    Submit('submit', 'Salvar', css_class=''),
                    Reset('reset', 'Limpar', css_class='btn-danger')
                )
            )
