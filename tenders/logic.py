from abc import ABC, abstractmethod

import requests


class IdReturner(ABC):
    """
    The main goal of the object of this class is to take API 'url' and
    the number of IDs that you want to return as a parameter, then
    return these IDs calling get_ids() method
    """
    def __init__(self, url: str, number_of_items_returned: int = 10):
        self.url = url
        self.number_of_items_returned = number_of_items_returned

    @abstractmethod
    def get_id_list(self):
        pass


class TendersIdReturner(IdReturner):

    def __get_tenders_list(self) -> list[dict]:
        """
        :return:
        a list of dictionaries, each dictionary contains two keys:
        {'dateModified' and 'id'}
        """
        response = requests.get(self.url)
        response.raise_for_status()
        tenders = response.json()
        tenders_data = tenders.get("data")
        return tenders_data

    def get_id_list(self) -> list[str]:
        """
        :return: a list where each element is tender_id
        """
        tenders_list = self.__get_tenders_list()
        list_of_tender_ids = [
            tender_dict.get("id")
            for tender_dict
            in tenders_list[:self.number_of_items_returned]
        ]

        return list_of_tender_ids


class ReturnCompleteTenders:

    def __init__(self, id_returner: IdReturner, tender_url: str):
        self.id_returner = id_returner
        self.tender_url = tender_url

    def get_ids(self):
        return self.id_returner.get_id_list()

    @staticmethod
    def __fetch_data_from_tender(tender: dict) -> dict:
        tender = tender.get("data")
        return tender

    @staticmethod
    def __fetch_description(tender: dict):
        return tender.get("description")

    @staticmethod
    def __fetch_amount(tender: dict):
        return tender.get("value").get("amount")

    @staticmethod
    def __fetch_date_last_modified(tender: dict):
        return tender.get("dateModified")

    @staticmethod
    def __fetch_id(tender: dict):
        return tender.get("id")

    def __fetch_all(self, tender_data):
        description = self.__fetch_description(tender_data)
        amount = self.__fetch_amount(tender_data)
        last_modified = self.__fetch_date_last_modified(tender_data)
        tender_id = self.__fetch_id(tender_data)

        final_tender = {
            "tender_id": tender_id,
            "description": description,
            "amount": amount,
            "date_modified": last_modified,
        }
        return final_tender

    def __get_tenders_from_id(self) -> list[dict]:
        complete_tenders = []

        for tender_id in self.get_ids():
            single_tender_url = self.tender_url + tender_id
            response = requests.get(single_tender_url)
            single_tender = response.json()
            complete_tenders.append(single_tender)

        return complete_tenders

    def return_tenders(self) -> list[dict]:
        """
        :return: list of dictionaries, where each dictionary has fields
        tender_id, description, amount, date_modified
        """
        tenders = self.__get_tenders_from_id()
        final_tenders = []

        for tender in tenders:
            tender_data = self.__fetch_data_from_tender(tender)
            tender = self.__fetch_all(tender_data)
            final_tenders.append(tender)

        return final_tenders
