import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file_path) as file_name:
            lista = file_name.read()
        return xmltodict.parse(lista)["dataset"]["record"]
