import pytest
from unittest.mock import patch, Mock
from src.hh_api import HeadHunterAPI


class TestHeadHunterAPI:
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        """Тест успешного получения вакансий"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [
                {
                    "name": "Python Dev",
                    "employer": {"name": "Company"},
                    "salary": {"from": 100000, "to": 150000},
                    "alternate_url": "http://example.com",
                    "snippet": {"requirement": "Experience with Django"}
                }
            ]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python")
        assert len(vacancies) == 1
        assert vacancies[0]["title"] == "Python Dev"

    @patch('requests.get')
    def test_get_vacancies_failure(self, mock_get):
        """Тест обработки ошибки API"""
        mock_get.side_effect = Exception("API Error")
        api = HeadHunterAPI()
        with pytest.raises(Exception):
            api.get_vacancies("Python")
