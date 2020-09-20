from django.core.exceptions import ValidationError


# admin
# orm / sql
def validate_publisher_state(value):
    print(value)
    return
    raise ValidationError("validate xxx")