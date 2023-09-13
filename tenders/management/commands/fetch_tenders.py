import requests
from django.core.management.base import BaseCommand

from TenderTracker.settings import SINGLE_TENDER_URL, TENDER_LIST_URL
from tenders.logic import TendersIdReturner, ReturnCompleteTenders
from tenders.models import Tender


class Command(BaseCommand):
    help = "Fetch and store data from the external API"

    def handle(self, *args, **options):
        try:
            tenders_ids = TendersIdReturner(TENDER_LIST_URL, 10)
            tenders = ReturnCompleteTenders(tenders_ids, SINGLE_TENDER_URL)
            tenders = tenders.return_tenders()
            Tender.create_tenders(tenders)
        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
