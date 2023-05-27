from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products: list[dict]) -> str:
        date = datetime.today().strftime("%Y-%m-%d")
        latest = min(
            product["data_de_fabricacao"] for product in products
        )
        expiration = min(
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"] > date
        )
        industry = [product["nome_da_empresa"] for product in products]

        biggest_industry = max(set(industry), key=industry.count)

        return (
            f"Data de fabricação mais antiga: {latest}\n"
            f"Data de validade mais próxima: {expiration}\n"
            f"Empresa com mais produtos: {biggest_industry}"
        )
