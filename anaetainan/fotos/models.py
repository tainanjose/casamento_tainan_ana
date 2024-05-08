from django.db import models

from django.utils.translation import gettext as _


class Fotos(models.Model):
    titulo = models.CharField(_("Titulo"), max_length=128, blank=True, default="")
    imagem = models.URLField(_("imagem"), blank=True, default="", max_length=1024)
    imagem_data = models.TextField(_("imagem data"), blank=True, null=True)
    ordem = models.IntegerField(blank=True, default=1, null=True)

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Fotos")

    def __str__(self):
        return self.titulo

    @property
    def imagem_src(self):
        return self.imagem_data if self.imagem_data else self.imagem
