from django.urls import path

from tenders.views import TenderListView

urlpatterns = [
    path(
        "",
        TenderListView.as_view(),
        name="tender-list"
    ),
]

app_name = "tenders"
