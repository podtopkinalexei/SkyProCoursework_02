from unittest.mock import patch

from main import user_interaction


class TestIntegration:
    @patch('main.HeadHunterAPI')
    @patch('main.JSONHandler')
    @patch('builtins.input')
    def test_full_flow(self, mock_input, mock_json, mock_api):
        """Тест полного цикла взаимодействия"""
        # Настройка моков
        mock_api.return_value.get_vacancies.return_value = [
            {
                "title": "Python Dev",
                "company": "Tech",
                "salary_from": 100000,
                "salary_to": 150000,
                "url": "http://example.com",
                "description": "Django experience"
            }
        ]

        # Эмулируем пользовательский ввод
        mock_input.side_effect = [
            "Python",  # Ключевое слово
            "10",  # Количество вакансий
            "5",  # Топ N
            "",  # Ключевые слова (пусто)
            ""  # Диапазон зарплат (пусто)
        ]

        # Запускаем основной поток
        user_interaction()

        # Проверяем вызовы
        mock_api.return_value.get_vacancies.assert_called_once_with("Python", 10)
        mock_json.return_value.add_to_file.assert_called_once()
