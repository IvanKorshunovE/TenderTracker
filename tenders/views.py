from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, DecimalField
from django.views.generic import ListView

from tenders.logic import TendersIdReturner, ReturnCompleteTenders
from tenders.models import Tender

TENDER_LIST_URL = "https://public.api.openprocurement.org/api/0/tenders?descending=1"
SINGLE_TENDER_URL = "https://public.api.openprocurement.org/api/0/tenders/"


class TenderListView(LoginRequiredMixin, ListView):
    model = Tender
    template_name = "tenders/tender_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        tenders_ids = TendersIdReturner(TENDER_LIST_URL, 10)  # returns a list of tenders ID
        tenders = ReturnCompleteTenders(tenders_ids, SINGLE_TENDER_URL)
        tenders = tenders.return_tenders()  # returns list of tenders dictionaries

        # Tender.create_tenders(tenders)
        tenders = Tender.objects.all()

        total_amount_result = Tender.objects.aggregate(
            total_amount=Sum(
                "amount", output_field=DecimalField()
            )
        )
        total_amount = total_amount_result.get("total_amount")
        total_amount = round(total_amount, 2)
        total_amount = "{:,.2f}".format(total_amount)

        context["tenders"] = tenders
        context["total_amount"] = total_amount
        return context
