import pytest
from main import filter_vacancies, get_vacancies_by_salary
from src.vacancy import Vacancy


class TestFilters:
    @pytest.fixture
    def sample_vacancies(self):
        return [
            Vacancy("Python Dev", "A", 100000, 150000, "url1", "Django experience"),
            Vacancy("Java Dev", "B", 90000, None, "url2", "Spring framework"),
            Vacancy("Data Scientist", "C", None, 200000, "url3", "Python and ML")
        ]

    def test_filter_by_keywords(self, sample_vacancies):
        """Тест фильтрации по ключевым словам"""
        filtered = filter_vacancies(sample_vacancies, ["python"])
        assert len(filtered) == 2
        assert all("Python" in v.title or "Python" in v.description for v in filtered)


    def test_empty_filters(self, sample_vacancies):
        """Тест пустых фильтров"""
        assert len(filter_vacancies(sample_vacancies, [])) == 3
        assert len(get_vacancies_by_salary(sample_vacancies, "")) == 3
