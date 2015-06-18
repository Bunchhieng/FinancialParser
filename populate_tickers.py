import csv

__author__ = 'Bunchhieng'
"""
    Populate name and ticker of Yahoo Finance into Symbol model
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kronos.settings')

import django

django.setup()

from finance_parser.models import Symbol

TICKERS = 'tickers.csv'


def populate():
    with open(TICKERS, errors='ignore') as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            add_ticker(str(row[1]), str(row[0]), row[2], str(row[3]), str(row[4]), row[5])


def add_ticker(name, symbol, IPOYear, sector, industry, summary_quote):
    c = Symbol.objects.get_or_create(name=name,
                                     symbol=symbol,
                                     IPOYear=IPOYear,
                                     sector=sector,
                                     industry=industry,
                                     summary_quote=summary_quote)
    return c


if __name__ == '__main__':
    populate()
    print("Completed!")
