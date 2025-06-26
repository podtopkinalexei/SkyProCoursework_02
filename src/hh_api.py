from typing import List, Dict, Any

import requests

from src.abstract_classes import JobAPI


class HeadHunterAPI(JobAPI):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HHVacancyParser/1.0'}
        self.__connected = False

    def connect(self) -> None:
        """Приватный метод подключения к API"""
        try:
            response = requests.get(self.__base_url, headers=self.__headers)
            response.raise_for_status()
            self.__connected = True
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Ошибка подключения к API HH: {e}")

    def get_vacancies(self, keyword: str, per_page: int = 100) -> List[Dict[str, Any]]:
        """
        Получение вакансий по ключевому слову

        :param keyword: Ключевое слово для поиска
        :param per_page: Количество вакансий на странице
        :return: Список вакансий
        """
        if not self.__connected:
            self.connect()

        params = {
            'text': keyword,
            'per_page': min(per_page, 100),
            'locale': 'RU'
        }

        try:
            response = requests.get(self.__base_url, params=params, headers=self.__headers)
            response.raise_for_status()
            data = response.json()
            return self._parse_vacancies(data.get('items', []))
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Ошибка при запросе вакансий: {e}")

    def _parse_vacancies(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Приватный метод парсинга вакансий"""
        parsed_vacancies = []
        for item in items:
            salary = item.get('salary')
            vacancy = {
                'title': item.get('name'),
                'company': item.get('employer', {}).get('name'),
                'salary_from': salary.get('from') if salary else None,
                'salary_to': salary.get('to') if salary else None,
                'url': item.get('alternate_url'),
                'description': item.get('snippet', {}).get('requirement', '')
            }
            parsed_vacancies.append(vacancy)
        return parsed_vacancies
