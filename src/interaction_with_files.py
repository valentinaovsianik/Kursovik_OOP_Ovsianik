import json
import os
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        """Добавление вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict) -> list:
        """Получение вакансий из файла по указанным критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: dict):
        """Удаление информации о вакансии из файла"""
        pass


class JSONFileHandler(FileHandler):
    """Класс для работы с JSON-файлами, наследующийся от абстрактного класса FileHandler"""

    def __init__(self, filename: str = "vacancies.json"):
        """Инициализация объекта JSONFileHandler с указанием имени файла"""
        self._directory = os.path.join(os.getcwd(), "data")
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)
        self._filename = os.path.join(self._directory, filename)

    def _load_data(self) -> list:
        """Загрузка данных из JSON-файла"""
        if os.path.exists(self._filename):
            with open(self._filename, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def _save_data(self, data: list):
        """Сохранение данных в JSON-файл"""
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: dict):
        """Добавление вакансии в JSON-файл."""
        data = self._load_data()
        if vacancy not in data:
            data.append(vacancy)
            self._save_data(data)

    def get_vacancies(self, criteria: dict) -> list:
        """Получение вакансий из JSON-файла по указанным критериям"""
        data = self._load_data()
        result = []
        for vacancy in data:
            match = True
            for key, value in criteria.items():
                if vacancy.get(key) != value:
                    match = False
                    break
            if match:
                result.append(vacancy)
        return result

    def delete_vacancy(self, vacancy: dict):
        """Удаление вакансии из JSON-файла"""
        data = self._load_data()
        if vacancy in data:
            data.remove(vacancy)
            self._save_data(data)
