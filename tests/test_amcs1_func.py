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

from amcs1.func import get_item


def test_item_price_is_decimal():
    item = get_item(1)
    assert type(item.get("price")) is Decimal


def test_item_price_is_10_34():
    item = get_item(1)
    assert item.get("price") == Decimal("10.34")


def test_item_price_is_not_10_35():
    item = get_item(1)
    assert item.get("price") != Decimal("10.35")


def test_item_currency_is_eur():
    item = get_item(1)
    assert item.get("price") == Decimal("10.34")
