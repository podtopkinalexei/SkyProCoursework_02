import pytest
from src.vacancy import Vacancy


class TestVacancy:
    def test_vacancy_creation(self):
        """Тест корректного создания вакансии"""
        vacancy = Vacancy(
            title="Python Developer",
            company="TechCorp",
            salary_from=100000,
            salary_to=150000,
            url="http://example.com",
            description="Backend development"
        )
        assert vacancy.title == "Python Developer"
        assert vacancy.salary_from == 100000
        assert vacancy.salary_to == 150000


    def test_to_dict(self):
        """Тест преобразования в словарь"""
        vacancy = Vacancy("Dev", "Co", 100000, 150000, "url", "desc")
        data = vacancy.to_dict()
        assert data["title"] == "Dev"
        assert data["salary_from"] == 100000

    def test_validation(self):
        """Тест валидации данных"""
        with pytest.raises(ValueError):
            Vacancy(123, "Co", 100000, 150000, "url", "desc")  # Неправильный title
