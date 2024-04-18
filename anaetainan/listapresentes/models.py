from django.utils.translation import gettext as _
from django.db import models


class Presente(models.Model):
    titulo = models.CharField(_("Título"), blank=True, max_length=128, default="")
    descricao = models.TextField(_("Descrição do presente"), blank=True, default="")
    imagem = models.URLField(_("imagem"), blank=True, default="", max_length=1024)
    valor = models.DecimalField(
        _("Valor"), max_digits=12, decimal_places=2, default=0.00
    )

    class Meta:
        verbose_name = _("Presente")
        ordering = ("valor",)

    def __str__(self):
        return "{0} (R${1})".format(self.titulo, self.valor)


class IntencaoDePresente(models.Model):
    data = models.DateTimeField(auto_now_add=True, editable=False)
    presente = models.ForeignKey(
        Presente, verbose_name=_("presente"), on_delete=models.CASCADE
    )
    nome = models.CharField(_("Seu nome"), default="", max_length=128)
    email = models.EmailField(_("e-mail"), max_length=128)
    banco = models.ForeignKey(
        "ContaParaRecebimento", on_delete=models.CASCADE, null=True
    )
    mensagem = models.TextField(_("Mensagem para o casal"), blank=True, default="")
    valor = models.DecimalField(
        _("Valor"), max_digits=12, decimal_places=2, default=0.00
    )
    pagamento_ok = models.BooleanField(default=False)
    saque_ok = models.BooleanField(default=False)
    agradecimento_ok = models.BooleanField(default=False)
    foto_agradecimento_ok = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Intenção de Presente")
        ordering = (
            "pagamento_ok",
            "banco",
            "saque_ok",
            "agradecimento_ok",
            "-id",
        )

    def __str__(self):
        ok = " [OK]" if self.pagamento_ok else " --> [VER CONTA]"
        ok += " [$$$acado] " if self.saque_ok else ""
        ok += " [Tks] " if self.agradecimento_ok else ""
        return "{0} ({1},{2}) - {3}".format(self.nome, self.valor, self.banco, ok)

    @property
    def centavos(self):
        return float(str(self.valor - int(self.valor))[1:])


class ContaParaRecebimento(models.Model):
    nome_banco = models.CharField(_("Banco"), blank=True, max_length=128, default="")
    agencia = models.CharField(_("Agencia"), blank=True, max_length=32, default="")
    conta = models.CharField(_("Conta"), blank=True, max_length=32, default="")
    favorecido = models.CharField(_("Favorecido"), blank=True, max_length=64, default="")
    cpf = models.CharField(_("CPF"), blank=True, max_length=32, default="")
    chave_pix = models.CharField(_("Chave PIX"), blank=True, max_length=128, default="")

    class Meta:
        verbose_name = _("Contas")
        ordering = ("id",)

    def __str__(self):
        return f"{self.nome_banco}"
