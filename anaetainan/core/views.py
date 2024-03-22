# coding: utf-8
import logging

from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.shortcuts import redirect, reverse

from ..fotos.models import Fotos

logger = logging.getLogger(__name__)


class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(ShowHomeView, self).get_context_data(**kwargs)

        if settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE:
            self.template_name = "core/home_savethedate.html"

        context[
            "DJ_CASAMENTO_MODO_SAVE_THE_DATE"
        ] = settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE
        context["DJ_CASAMENTO_DE_UM_LADO"] = settings.DJ_CASAMENTO_DE_UM_LADO
        context["DJ_CASAMENTO_DO_OUTRO"] = settings.DJ_CASAMENTO_DO_OUTRO
        context["DJ_CASAMENTO_DATA"] = settings.DJ_CASAMENTO_DATA
        context["DJ_CASAMENTO_LOCAL"] = settings.DJ_CASAMENTO_LOCAL
        context["DJ_CASAMENTO_CIDADE"] = settings.DJ_CASAMENTO_CIDADE
        context["DJ_CASAMENTO_DATE"] = settings.DJ_CASAMENTO_DATE
        context["DJ_CASAMENTO_JA_ACONTECEU"] = settings.DJ_CASAMENTO_JA_ACONTECEU
        context["DJ_CASAMENTO_EMAIL_CONTATO"] = settings.DJ_CASAMENTO_EMAIL_CONTATO
        context["DJ_CASAMENTO_FONE_CONTATO"] = settings.DJ_CASAMENTO_FONE_CONTATO
        context["DJ_CASAMENTO_SERVER"] = settings.DJ_CASAMENTO_SERVER
        context["fotos"] = Fotos.objects.all().order_by("ordem")

        return context


class SaveTheDateView(TemplateView):
    template_name = "core/savethedate.html"

    def get_context_data(self, **kwargs):
        to = self.request.GET.get("to") or ""
        context = super(SaveTheDateView, self).get_context_data(**kwargs)
        context["to"] = to
        return context


class ConfirmacaoRedirectView(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        self.url = reverse("rsvp.confirmacaohome")
        return redirect(self.url)
