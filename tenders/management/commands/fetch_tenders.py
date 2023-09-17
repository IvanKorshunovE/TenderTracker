import requests
from django.core.management.base import BaseCommand

from TenderTracker.settings import (
    SINGLE_TENDER_URL,
    TENDER_LIST_URL,
    NUBER_OF_TENDERS_TO_DISPLAY
)
from tenders.logic import TendersIdReturner, ReturnCompleteTenders
from tenders.models import Tender


class Command(BaseCommand):
    """
    This command performs the following tasks:
    1. Deletes all existing tenders from the database.
    2. Retrieves the most recent tenders from the API.
    3. Stores these retrieved tenders in the local database.
    """
    help = "Fetch and store data from the external API"

    def handle(self, *args, **options):
        try:
            number_of_tenders = NUBER_OF_TENDERS_TO_DISPLAY
            tenders_ids = TendersIdReturner(TENDER_LIST_URL, number_of_tenders)
            tenders = ReturnCompleteTenders(tenders_ids, SINGLE_TENDER_URL)
            tenders = tenders.return_tenders()

            Tender.create_tenders(tenders)
        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
