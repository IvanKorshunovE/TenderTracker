from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from TenderTracker.settings import NUBER_OF_TENDERS_TO_DISPLAY
from tenders.models import Tender


class TenderListView(LoginRequiredMixin, ListView):
    model = Tender
    template_name = "tenders/tender_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tenders = self.get_queryset()[:NUBER_OF_TENDERS_TO_DISPLAY]

        total_amount = Tender.get_all_tenders_total_amount()
        total_amount = Tender.prettify_amount(total_amount)

        tenders_context = {
            "tenders": tenders,
            "total_amount": total_amount
        }
        context.update(tenders_context)
        return context
