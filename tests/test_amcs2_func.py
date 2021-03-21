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
from unittest.mock import patch

import responses
import pytest

from amcs2.func import calculate, do_exchange, get_item


@responses.activate
def test_get_item():
    responses.add(
        responses.GET,
        'http://dummy.url/10',
        json={
            'price': '20.9'
        },
        status=200
    )

    with patch('amcs2.func.amcs1_url', 'http://dummy.url/'):
        item = get_item(10)

    assert item == {"price": Decimal("20.9")}


def test_calculate():
    price = Decimal("23.10")
    exchange_rate = Decimal("1.19")
    c = calculate(price, exchange_rate)
    assert c == Decimal("27.4890")


def test_calculate_price_must_be_decimal():
    price = 23.10
    exchange_rate = Decimal("1.19")
    with pytest.raises(AssertionError):
        calculate(price, exchange_rate)


def test_calculate_exchange_rate_must_be_decimal():
    price = Decimal("23.10")
    exchange_rate = 1.19
    with pytest.raises(AssertionError):
        calculate(price, exchange_rate)


def test_do_exchange_format():
    item_id = 101

    item_eur = {
        "id": item_id,
        "price": Decimal("10.4"),
        "currency": "EUR"
    }

    price_usd = Decimal("10.0")

    expected_item_usd = {
        "id": item_id,
        "original": item_eur,
        "price": price_usd,
        "currency": "USD"
    }

    def mock_calculate(price, exchange_rate):
        return price_usd

    with patch('amcs2.func.calculate', mock_calculate):
        item_usd = do_exchange(item_eur)

    assert expected_item_usd == item_usd, \
        "Expected item doesn't share the same contents as generated item."


def test_do_exchange_no_price():
    item_eur = {
        "id": 101,
        "currency": "EUR"
    }

    with pytest.raises(AssertionError):
        do_exchange(item_eur)
