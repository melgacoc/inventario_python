from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report):
        data = self.importer.import_data(path)
        self.data.extend(data)

        if report == "simples":
            return SimpleReport.generate(data)
        if report == "complete":
            return CompleteReport.generate(data)

    def __iter__(self):
        return InventoryIterator(self.data)
