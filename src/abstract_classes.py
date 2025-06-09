from abc import ABC, abstractmethod
from typing import List, Dict, Any


class JobAPI(ABC):
    """Абстрактный класс для работы с API вакансий"""

    @abstractmethod
    def connect(self) -> None:
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод получения вакансий"""
        pass


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def read_file(self) -> List[Dict[str, Any]]:
        """Чтение данных из файла"""
        pass

    @abstractmethod
    def add_to_file(self, data: List[Dict[str, Any]]) -> None:
        """Добавление данных в файл"""
        pass

    @abstractmethod
    def delete_from_file(self, criteria: Dict[str, Any]) -> None:
        """Удаление данных из файла"""
        pass
