from django.db import models

from django.utils.translation import gettext as _


class Fotos(models.Model):
    titulo = models.CharField(_('Titulo'), max_length=128, blank=True, default='')
    imagem = models.ImageField(
        _('imagem'), upload_to='fotos/', blank=True, default='')
    ordem = models.IntegerField(blank=True, default=1, null=True)

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Fotos")

    def __str__(self):
        return self.titulo
