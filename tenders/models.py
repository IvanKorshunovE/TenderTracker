from django.db import models
from django.db.models import Sum, DecimalField


class Tender(models.Model):
    tender_id = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_modified = models.DateTimeField()

    @classmethod
    def create_tenders(cls, tender_list: list[dict]):
        Tender.objects.all().delete()
        tenders = [
            Tender(**tender_data)
            for tender_data
            in tender_list
        ]
        Tender.objects.bulk_create(tenders)

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
        total_amount = round(total_amount, 2)
        total_amount = "{:,.2f}".format(total_amount)
        return total_amount

    def __repr__(self):
        return str(self.tender_id)

    def __str__(self):
        return str(self.tender_id)

    @property
    def display_description(self):
        if self.description:
            return self.description
        return "No description available"

    @property
    def display_amount(self):
        return "{:,.2f}".format(self.amount)

    class Meta:
        ordering = ["-date_modified"]
