# AMCS
# Copyright (C) 2021 Yennick Schepers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from decimal import Decimal

import requests

from .config import amcs1_url, exchange_rate_eur_usd


def get_item(item_id):
    """
    Get item resource from external REST resource and parse it.

    :param item_id: The identifier of the item to get.
    :type item_id: int
    :return: The requested item.
    :rtype: dict
    :raises Exception: Undocumented eceptions

    Note: Consuming an external resource, proper error handling shoud be
    provided for this.
    """
    r = requests.get(f"{amcs1_url}{item_id}")
    item = r.json()

    item.update({
        "price": Decimal(item['price'])
    })

    return item


def calculate(price, exchange_rate):
    """
    Calculates a price based on price and exchange rate.

    :param price: The price in the original currency.
    :type price: Decimal
    :param exchange_rate: The exchange rate to apply.
    :type exchange_rate: Decimal
    :return: The price in the new currency.
    :rtype Decimal:
    """
    assert type(price) is Decimal, "The price must be a Decimal."
    assert type(exchange_rate) is Decimal,\
        "The exchange rate must be a Decimal."

    return price * exchange_rate


def do_exchange(item):
    """
    Exchanges the price of am item from EUR to USD.

    :param item: The item to exchange
    :type item: dict
    :return: new currency item.
    :rtype: dict

    Note: More validation of the data structure should happen.
    """
    assert "id" in item, "The item doesn't have an identifier."
    assert "price" in item, "The item doesn't have a price."
    price = item["price"]
    exchange_rate = exchange_rate_eur_usd

    return {
        "id": item["id"],
        "price": calculate(price, exchange_rate),
        "currency": "USD",
        "original": item
    }


def get_exchange(item_id):
    """
    Get the item for from an external resource for identifier item_id.

    :param item_id: The identifier for the key to apply the exchange rate for.
    :type item_id: int
    :return: The requested item with the exchange rate applied.
    :rtype: dict
    """
    item = get_item(item_id)
    return do_exchange(item)
