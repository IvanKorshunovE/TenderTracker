from django.db import models


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

    def __repr__(self):
        return self.tender_id

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["-date_modified"]
