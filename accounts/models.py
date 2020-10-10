from django.db import models
from django.contrib.auth.models import AbstractUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Reset
from crispy_forms.bootstrap import Accordion, AccordionGroup, Alert, AppendedText, FieldWithButtons, InlineCheckboxes, InlineRadios, PrependedAppendedText, PrependedText, StrictButton, Tab, TabHolder


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
