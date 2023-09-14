from django.db import models
from django.db.models import Sum, DecimalField


class Tender(models.Model):
    tender_id = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    date_modified = models.DateTimeField(null=True)

    @classmethod
    def create_tenders(cls, tender_list: list[dict]):
        existing_tender_ids = Tender.objects.values_list("tender_id", flat=True)

        tenders_to_create = []

        for tender_data in tender_list:
            tender_id = tender_data["tender_id"]

            if tender_id not in existing_tender_ids:
                tenders_to_create.append(Tender(**tender_data))

        Tender.objects.bulk_create(tenders_to_create)

    @classmethod
    def get_all_tenders_total_amount(cls):
        total_amount_result = Tender.objects.aggregate(
            total_amount=Sum(
                "amount", output_field=DecimalField()
            )
        )
        total_amount = total_amount_result.get("total_amount")
        return total_amount

    @staticmethod
    def prettify_amount(total_amount):
        if total_amount:
            total_amount = round(total_amount, 2)
            total_amount = "{:,.2f}".format(total_amount)
            return total_amount
        return "Enable to define the amount"

    def __repr__(self):
        return str(self.tender_id)

    def __str__(self):
        return str(self.tender_id)

    @property
    def display_description(self):
        if self.description:
            return self.description
        return "Description is not specified"

    @property
    def display_amount(self):
        if self.amount:
            return "{:,.2f}".format(self.amount)
        return "Amount is not specified"

    @property
    def display_date_modified(self):
        if self.amount:
            return self.prettify_amount(self.amount)
        return "Last update date is not specified"

    class Meta:
        ordering = ["-date_modified"]
