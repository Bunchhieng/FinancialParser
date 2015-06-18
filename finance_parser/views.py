import csv
import json
import re
import urllib

from bs4 import BeautifulSoup

from django.http import HttpResponse
from django.shortcuts import render

from .models import Symbol

"""
    Author: Bunchhieng Soth
    Created on: June 1st 2015
"""


def index(request):
    context_dict = {}
    symbols = Symbol.objects.all()
    context_dict['symbols'] = symbols
    context_dict['count'] = symbols.count()
    return render(request, 'finance_parser/index.html', context_dict)


def data(request, symbol):
    context_dict = {}

    gen_table = data_scrapper(symbol)

    # Match 'symbol' to 'name' in models
    name = Symbol.objects.get(symbol=symbol)

    # Add objects to context_dict
    context_dict['gen_table'] = str(gen_table)
    context_dict['symbol'] = symbol
    context_dict['name'] = name

    return render(request, 'finance_parser/data.html', context_dict)


def get_ticker(request):
    """
    This view return json for jQuery UI autocomplete search.
    :param request:
    :return: json file with symbol and name from Symbol models.
    """
    if request.is_ajax():
        q = request.GET.get('term', '')
        symbols = Symbol.objects.filter(name__istartswith=q)
        results = []
        for symbol in symbols:
            symbol_json = {'name': str(symbol.name), 'symbol': symbol.symbol}
            results.append(symbol_json)
        data = json.dumps(results)
    else:
        data = 'Can\'t get data...'

    mimetype = 'application/json'

    return HttpResponse(data, mimetype)


def button_clicked(request):
    rows = []
    # request.META['HTTP_REFERER']
    # http://127.0.0.1:8000/finance/PII/
    current_url = request.META['HTTP_REFERER']
    # Split `symbol` from current_url
    symbol = current_url[-4:-1]
    gen_table = data_scrapper(symbol)

    soup = BeautifulSoup(gen_table)
    table = soup.find("table")
    headers = [header.text for header in table.find_all('th')]
    for row in table.find_all('tr'):
        rows.append([val.text for val in row.find_all('td')])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "{}.csv"'.format(symbol)

    writer = csv.writer(response)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)

    return response


def data_scrapper(symbol):
    """
    This function scrap financial data from NASDAQ then parse with BeautifulSoup
    :param symbol: request symbol.
    :return: div contains income statement data.
    """
    NASDAQ = "http://www.nasdaq.com/symbol/{}/financials?query=income-statement".format(symbol)

    # Added user agent to bypass 403 forbidden from the server
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    try:
        assembled_request = urllib.request.Request(NASDAQ, None, headers)
        response = urllib.request.urlopen(assembled_request)
        html_data = response.read()  # The data u need

        # Using BeautifulSoup to scrap specific div in html data
        soup = BeautifulSoup(html_data)
        gen_table = soup.find_all("div", class_="genTable")
    except IOError as e:
        print(str(e))
    # remove unwanted "[]"
    gen_table = re.sub(r'[\[\]]', r'', str(gen_table))

    return gen_table
