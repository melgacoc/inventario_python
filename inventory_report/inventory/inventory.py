from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:
    pass

    @ staticmethod
    def import_data(file_name, report_type):
        report = CsvImporter.import_data(file_name)

        if report_type == "simples":
            return SimpleReport.generate(report)
        if report_type == "completo":
            return CompleteReport.generate(report)

        raise ValueError("Tipo de relatório inválido")
