from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class Vacancy:
    """Класс для представления вакансии"""
    __slots__ = ['title', 'company', 'salary_from', 'salary_to', 'url', 'description']

    title: str
    company: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    url: str
    description: str

    def __post_init__(self):
        self._validate_data()

    def _validate_data(self) -> None:
        """Приватный метод валидации данных"""
        if not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой")
        if self.salary_from is not None and not isinstance(self.salary_from, int):
            raise ValueError("Зарплата 'от' должна быть целым числом или None")
        if self.salary_to is not None and not isinstance(self.salary_to, int):
            raise ValueError("Зарплата 'до' должна быть целым числом или None")

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по минимальной зарплате"""
        self_salary = self.salary_from or 0
        other_salary = other.salary_from or 0
        return self_salary < other_salary

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по максимальной зарплате"""
        self_salary = self.salary_to or 0
        other_salary = other.salary_to or 0
        return self_salary > other_salary

    def to_dict(self) -> Dict[str, Any]:
        """Преобразование вакансии в словарь"""
        return {
            'title': self.title,
            'company': self.company,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'url': self.url,
            'description': self.description
        }
