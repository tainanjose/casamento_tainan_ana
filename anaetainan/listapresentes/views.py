from random import randint

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import Presente, IntencaoDePresente, ContaParaRecebimento
from .forms import IntencaoDePresenteForm


class PaginaPrincipalListView(ListView):
    model = Presente
    paginate_by = "100"
    context_object_name = "presente_list"


class IntencaoDePresenteCreateView(CreateView):
    model = IntencaoDePresente
    form_class = IntencaoDePresenteForm

    def get_initial(self):
        presente = get_object_or_404(Presente, pk=self.kwargs["pk"])
        initial = {
            "presente": presente,
            "contas": ContaParaRecebimento.objects.all().order_by('nome_banco'),
        }
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        centavos = randint(1, 99) / 100
        self.object.valor += centavos + float(self.object.presente.valor)
        self.object.save()
        url = reverse(
            "listapresentes.intencao.confirmacao", kwargs={"pk": self.object.id}
        )

        if settings.DJ_EMAIL_NOTIFICATIONS:
            email_body = "{0} teve uma intenção de presente {1} ({2}, {3})".format(
                self.object.nome, self.object.presente, self.object.valor, self.object.banco
            )

            title = f"{settings.DJ_CASAMENTO_DE_UM_LADO} & {settings.DJ_CASAMENTO_DO_OUTRO} - Presente"
            send_mail(
                title,
                email_body,
                settings.DJ_EMAIL_FROM,
                settings.DJ_EMAIL_DISTRIBUTION_LIST,
                fail_silently=False,
            )

        return HttpResponseRedirect(url)


class IntencaoDePresenteConfirmacaoView(UpdateView):
    model = IntencaoDePresente
    form_class = IntencaoDePresenteForm
    template_name = "listapresentes/intencaodepresente_confirmacao.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contas'] = ContaParaRecebimento.objects.all().order_by('nome_banco')
        return context
