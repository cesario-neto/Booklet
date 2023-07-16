from datetime import datetime
import csv
import os


class Booklet:
    def __init__(self):
        self.id = id
        self._current_date = self._get_current_date()

    def _get_current_date(self):
        date = datetime.now()
        formatted_date = date.strftime('%d-%m-%Y')
        return formatted_date

    def _creating_directory_for_csv(self):
        if not os.path.exists('csv_reports'):
            os.mkdir('csv_reports')
        return None

    def add_order(self, product: dict):
        self._creating_directory_for_csv()
        file_path = f'csv_reports/{self._current_date}.csv'
        with open(file_path, 'a', encoding='UTF-8', newline='') as csvfile:
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

    @property
    def get_current_date(self):
        return self._current_date
