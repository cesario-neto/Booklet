from datetime import datetime
import csv


class Booklet:
    def __init__(self):
        self.id = id
        self._current_date = self._get_current_date()

    def _get_current_date(self):
        date = datetime.now()
        formatted_date = date.strftime('%d-%m-%Y')
        return formatted_date

    @property
    def get_current_date(self):
        return self._current_date

    def add_order(self, product: dict):
        with open(f'csv_reports/{self._current_date}.csv', 'a', encoding='UTF-8', newline='') as csvfile:
            fieldnames = ['product', 'price', 'quantity', 'type_of_sale']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({
                'product': product['product'],
                'price': product['price'],
                'quantity': product['quantity'],
                'type_of_sale': product['type_of_sale']
            })

        return None
