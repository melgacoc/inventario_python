import csv
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            products = csv.DictReader(file, delimiter=",")
            return [product for product in products]
