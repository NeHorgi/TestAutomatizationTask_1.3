import requests
import pytest
from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import List


@dataclass
class CompanyInfo:
    name: str
    popularity: int
    front: str
    back: str
    database: str
    notes: str = None


@pytest.fixture
def parsing_a_table() -> List:

    url = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')
    soup = BeautifulSoup(url.text, "html.parser")
    wiki_table = soup.table

    parsed_table_from_wiki = []

    for table_row in wiki_table.find_all('tr'):
        iteration = 0
        count = 0
        string_from_table = []

        for table_row_column in table_row.find_all('td'):
            iteration += 1
            while count != 1000000:
                if table_row_column.select_one('sup'):
                    table_row_column.select_one('sup', class_='reference').decompose()
                else:
                    break
                count += 1
            if iteration == 2:
                population_column = table_row_column.get_text(strip=True).replace('.', ',').replace(',', '').split(' ')
                if len(population_column) == 1:
                    string_from_table.append(int(*population_column))
                    continue
                else:
                    for elem in population_column:
                        chosen_one = ''
                        try:
                            chosen_one = int(elem)
                            break
                        except ValueError:
                            pass
                    string_from_table.append(int(chosen_one))
                    continue
            string_from_table.append(table_row_column.get_text(strip=True))

        if string_from_table:
            parsed_table_from_wiki.append(CompanyInfo(*[table_column for table_column in string_from_table]))

    return parsed_table_from_wiki

