# from django.utils.translation import gettext as _

import floppyforms.__future__ as forms

# from floppyforms.widgets import EmailInput, TextInput

from .models import IntencaoDePresente


class IntencaoDePresenteForm(forms.ModelForm):
    class Meta:
        model = IntencaoDePresente
        fields = (
            "presente",
            "nome",
            "email",
            "banco",
            "mensagem",
        )
        help_texts = {
            "email": "Informe um email para enviarmos a confirmação.",
        }
