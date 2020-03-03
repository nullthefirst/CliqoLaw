from django.forms import ModelForm
from .models import NewMatter, ClientInfo, CollaboratorInfo, Outcomes


class NewMatterForm(ModelForm):
    class Meta:
        model = NewMatter
        fields = ['reference_number', 'nature_of_matter', 'price_estimate', 'hourly_rate']


class ClientInfoForm(ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['ref', 'client_name', 'contact_phone', 'contact_email', 'contact_address']


class CollaboratorInfoForm(ModelForm):
    class Meta:
        model = CollaboratorInfo
        fields = ['ref', 'full_name', 'phone_number', 'role', 'email']


class OutcomesForm(ModelForm):
    class Meta:
        model = Outcomes
        fields = ['goal']
