import json
import os
from pathlib import Path
from typing import List, Dict, Any


class JSONHandler:
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = 'data/vacancies.json'):
        self.__filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Создает файл и директорию если они не существуют"""
        try:
            # Создаем директорию если ее нет
            Path(self.__filename).parent.mkdir(parents=True, exist_ok=True)

            # Создаем файл если его нет
            if not os.path.exists(self.__filename):
                with open(self.__filename, 'w', encoding='utf-8') as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
        except (IOError, OSError) as e:
            raise RuntimeError(f"Не удалось создать файл: {e}")

    def read_file(self) -> List[Dict[str, Any]]:
        """
        Чтение данных из файла
        Возвращает пустой список при ошибках чтения
        """
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def add_to_file(self, data: List[Dict[str, Any]]) -> None:
        """Добавляет данные в файл, исключая дубликаты"""
        if not data:
            return

        try:
            existing_data = self.read_file()
            existing_urls = {item['url'] for item in existing_data if 'url' in item}

            # Фильтрация новых данных
            new_data = [
                item for item in data
                if isinstance(item, dict) and 'url' in item and item['url'] not in existing_urls
            ]

            if not new_data:
                return

            # Объединение и сохранение данных
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(existing_data + new_data, f, ensure_ascii=False, indent=4)

        except Exception as e:
            raise RuntimeError(f"Ошибка при добавлении данных: {e}")

    def delete_from_file(self, criteria: Dict[str, Any]) -> None:
        """Удаляет данные из файла по указанным критериям"""
        if not criteria:
            return

        try:
            data = self.read_file()
            filtered_data = [
                item for item in data
                if not all(item.get(k) == v for k, v in criteria.items())
            ]

            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(filtered_data, f, ensure_ascii=False, indent=4)

        except Exception as e:
            raise RuntimeError(f"Ошибка при удалении данных: {e}")

    def clear_file(self) -> None:
        """Полностью очищает файл"""
        try:
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError(f"Ошибка при очистке файла: {e}")
