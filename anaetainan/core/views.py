# coding: utf-8
import logging

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)
from django.views.decorators.http import require_http_methods

from ..commons.django_views_utils import ajax_login_required


from .service import tasks_svc

from django.views.generic import TemplateView
from django.conf import settings




@csrf_exempt
@ajax_login_required
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



@require_http_methods(["GET"])
@ajax_login_required

def list_tasks(request):
    logger.info("API list tasks")
    tasks = tasks_svc.list_tasks()
    return JsonResponse({"tasks": tasks})


class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(ShowHomeView, self).get_context_data(**kwargs)

        if settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE:
            self.template_name = "core/home_savethedate.html"

        context['fotos'] = Fotos.objects.all().order_by('ordem')

        return context