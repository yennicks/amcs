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

from fastapi import FastAPI

from .func import get_exchange


app = FastAPI()


@app.get("/exchange/{item_id}")
def read_exchange(item_id: int):
    """
    Get the item for from an external resource for identifier item_id.

    :param item_id: The identifier for the key to apply the exchange rate for.
    :type item_id: int
    :return: The requested item with the exchange rate applied.
    :rtype: dict
    """
    return get_exchange(item_id)
