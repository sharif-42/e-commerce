from django.utils.translation import gettext_lazy as _


class ColorOptions:
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    BLACK = 'black'
    WHITE = 'white'
    ORANGE = 'orange'
    YELLOW = 'yellow'

    CHOICES = (
        (RED, _("Red")),
        (GREEN, _("Green")),
        (BLUE, _("Blue")),
        (BLACK, _("Black")),
        (WHITE, _("White")),
        (ORANGE, _("Orange")),
        (YELLOW, _("Yellow")),
    )
