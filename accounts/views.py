from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
