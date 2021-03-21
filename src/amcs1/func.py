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


def get_item(item_id):
    """
    Get the item based on item_id.

    :param item_id: The identifier of the item.
    :type item_id: int
    :return: The requested item.
    :rtype: dict
    """
    return {
        "id": item_id,
        "price": Decimal("10.34"),
        "currency": "EUR"
    }
