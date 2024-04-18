from django.contrib import admin

from .models import Presente, IntencaoDePresente, ContaParaRecebimento


admin.site.register(Presente)
admin.site.register(IntencaoDePresente)
admin.site.register(ContaParaRecebimento)
