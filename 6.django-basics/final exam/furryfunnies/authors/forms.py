from django import forms

from furryfunnies.authors.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['info', 'image_url']
        labels = {
            'first_name': 'First Name:',   
            'last_name': 'Last Name:',     
            'passcode': 'Passcode:',       
            'pets_number': 'Pets Number:',  
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
    help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits',
        }


class DeleteAuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Author
        fields = ()

class EditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['passcode']
    image_url = forms.URLField(
        label='Publish Image URL:',)