import requests
import pytest
from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import List

import ParcingTableFromWiki

parameters_for_test = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
parsed_table = ParcingTableFromWiki.parsing_a_table


@pytest.mark.parametrize('parameter', parameters_for_test)
def test_parametrize_task_1(parameter, parsed_table):

    errors = []

    for table_row in parsed_table:

        if parameter > table_row.popularity:
            errors.append(f'{table_row.name} (Frontend:{table_row.front}|Backend:{table_row.back}) has {table_row.popularity} unique visitors per month. (Expected less than {parameter})')

    assert not errors, '\n'.join(errors)

