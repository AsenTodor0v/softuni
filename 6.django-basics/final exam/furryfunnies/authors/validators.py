from django.forms import ValidationError


def only_letters(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")
    

def exact_length(value):
    if len(value) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")