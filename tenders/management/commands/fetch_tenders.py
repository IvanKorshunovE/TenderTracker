import requests
from django.core.management.base import BaseCommand
from tenders.models import Tender


class Command(BaseCommand):
    help = "Fetch and store data from the external API"

    def handle(self, *args, **options):
        api_url = "https://public.api.openprocurement.org/api/0/tenders?descending=1"
        print("Hello world")

        # try:
        #     response = requests.get(api_url)
        #     response.raise_for_status()
        #
        #     data = response.json()
        #
        #     # Process and save the data to your local database
        #     for tender_data in data:
        #         tender = Tender(
        #             tender_id=tender_data["tender_id"],
        #             description=tender_data["description"],
        #             amount=tender_data['amount']['value'],
        #             dateModified=tender_data['dateModified']
        #         )
        #         tender.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully fetched and stored data.'))
        # except requests.exceptions.RequestException as e:
        #     self.stderr.write(self.style.ERROR(f'Error: {e}'))
