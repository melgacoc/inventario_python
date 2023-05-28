from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    pass

    @ staticmethod
    def import_data(file_name, report_type):
        report = Inventory.file_format(file_name)

        if report_type == "simples":
            return SimpleReport.generate(report)
        if report_type == "completo":
            return CompleteReport.generate(report)

        raise ValueError("Tipo de relatório inválido")

    @staticmethod
    def file_format(file_name):
        if file_name.endswith("csv"):
            return CsvImporter.import_data(file_name)
        if file_name.endswith("json"):
            return JsonImporter.import_data(file_name)
