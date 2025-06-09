import pytest
import os
from tempfile import NamedTemporaryFile
from src.json_handler import JSONHandler


class TestJSONHandler:
    @pytest.fixture
    def temp_file(self):
        with NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8') as f:
            yield f.name
        os.unlink(f.name)

    def test_add_and_read(self, temp_file):
        """Тест добавления и чтения данных"""
        handler = JSONHandler(temp_file)
        test_data = [{"title": "Dev", "url": "http://example.com"}]

        handler.add_to_file(test_data)
        data = handler.read_file()

        assert len(data) == 1
        assert data[0]["title"] == "Dev"

    def test_no_duplicates(self, temp_file):
        """Тест отсутствия дубликатов"""
        handler = JSONHandler(temp_file)
        data1 = [{"title": "Dev", "url": "http://example.com"}]
        data2 = [{"title": "Dev", "url": "http://example.com"}]

        handler.add_to_file(data1)
        handler.add_to_file(data2)

        assert len(handler.read_file()) == 1

    def test_delete_data(self, temp_file):
        """Тест удаления данных"""
        handler = JSONHandler(temp_file)
        test_data = [
            {"title": "Dev1", "url": "url1"},
            {"title": "Dev2", "url": "url2"}
        ]

        handler.add_to_file(test_data)
        handler.delete_from_file({"title": "Dev1"})

        data = handler.read_file()
        assert len(data) == 1
        assert data[0]["title"] == "Dev2"
