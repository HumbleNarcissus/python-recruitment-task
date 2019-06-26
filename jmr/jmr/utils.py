import string
import random
from .models import Site


def create_shortcut():
    """
    Generate new random site code
    """
    new_shortcut = ''.join(random.choices(
        string.ascii_uppercase + string.ascii_lowercase + string.digits,
        k=10)
    )

    for item in Site.objects.all():
        if item.shortcut == new_shortcut:
            return create_shortcut()

    return new_shortcut