from django import forms
from myapp1.models import OrderItem, Item
from django.contrib.auth.forms import AuthenticationForm

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['client', 'items_ordered', 'item']
        widgets = {
            'client': forms.RadioSelect,
            'item':forms.RadioSelect,
        }
        labels = {
            'client': 'Client Name',
            'items_ordered': 'Quantity',
            'item': 'Item'
        }


class InterestForm(forms.Form):
    interested = forms.BooleanField(required=False, label='interested', widget=forms.RadioSelect(choices=((1, 'Yes'), (0, 'No'))))
    quantity = forms.IntegerField(label='Quantity', initial=1, min_value=1)
    comments = forms.CharField(label='Additional Comments', widget=forms.Textarea, required=False)



# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'autofocus': True}))
#     password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)
#
#     error_messages = {
#         'invalid_login': 'Please enter a correct %(username)s and password. Note that both fields may be case-sensitive.'
#     }