from django.views.generic import ListView

from .models import Fornecedor


class FornecedoresListView(ListView):
    model = Fornecedor
    paginate_by = "100"
