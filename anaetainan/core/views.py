# coding: utf-8
import logging

import json

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings

logger = logging.getLogger(__name__)

from .service import tasks_svc
from ..fotos.models import Fotos


def add_task(request):
    logger.info("API add new task.")
    body = json.loads(request.body)
    description = body.get("description")

    if not description:
        raise ValueError("body.task.description: field required (value_error.missing)")
    if type(description) not in [str, int]:
        raise ValueError("body.task.description: str type expected (type_error.str)")

    description = str(description)
    if len(description) <= 2:
        raise ValueError(
            "body.task.description: It must be at least 3 characteres long. (value_error)"
        )

    new_task = tasks_svc.add_task(description)

    return JsonResponse(new_task, status=201)





class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(ShowHomeView, self).get_context_data(**kwargs)

        if settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE:
            self.template_name = "core/home_savethedate.html"

        context['DJ_CASAMENTO_MODO_SAVE_THE_DATE'] = settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE
        context['DJ_CASAMENTO_DE_UM_LADO'] = settings.DJ_CASAMENTO_DE_UM_LADO
        context['DJ_CASAMENTO_DO_OUTRO'] = settings.DJ_CASAMENTO_DO_OUTRO
        context['DJ_CASAMENTO_DATA'] = settings.DJ_CASAMENTO_DATA
        context['DJ_CASAMENTO_LOCAL'] = settings.DJ_CASAMENTO_LOCAL
        context['DJ_CASAMENTO_CIDADE'] = settings.DJ_CASAMENTO_CIDADE
        context['DJ_CASAMENTO_DATE'] = settings.DJ_CASAMENTO_DATE
        context['DJ_CASAMENTO_JA_ACONTECEU'] = settings.DJ_CASAMENTO_JA_ACONTECEU
        context['DJ_CASAMENTO_EMAIL_CONTATO'] = settings.DJ_CASAMENTO_EMAIL_CONTATO
        context['DJ_CASAMENTO_FONE_CONTATO'] = settings.DJ_CASAMENTO_FONE_CONTATO
        context['DJ_CASAMENTO_SERVER'] = settings.DJ_CASAMENTO_SERVER
        context['fotos'] = Fotos.objects.all().order_by('ordem')

        return context