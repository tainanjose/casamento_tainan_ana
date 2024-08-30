# coding: utf-8
import logging

from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.shortcuts import reverse

from ..fotos.models import Fotos

from django.shortcuts import render, redirect
from .models import QuizResult


logger = logging.getLogger(__name__)


class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(ShowHomeView, self).get_context_data(**kwargs)

        show_std = (
            not self.request.user.is_superuser
            and settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE
        )
        if show_std:
            self.template_name = "core/home_savethedate.html"

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


def quiz_view(request):
    if request.method == "POST":
        correct_answers = {
            "q1": "B",
            "q2": "C",
            "q3": "A",
            "q4": "B",
            "q5": "B",
            "q6": "A",
            "q7": "A",
        }
        score = 0
        nome = request.POST.get("nome")
        time = request.POST.get("time")

        for question, correct_answer in correct_answers.items():
            if request.POST.get(question) == correct_answer:
                score += 1

        # Salva o resultado no banco de dados
        result = QuizResult(nome=nome, time=time, score=score)
        result.save()

        # Redireciona para a página de resultados
        return redirect("quiz_result")

    return render(request, "quiz.html")


def quiz_result(request):
    ranking = QuizResult.objects.all().order_by("-score")  # Ordena pelo score
    return render(request, "quiz_result.html", {"ranking": ranking})
