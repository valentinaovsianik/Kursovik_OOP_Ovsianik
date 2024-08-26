import json
from abc import ABC, abstractmethod

import requests


class JobAPI(ABC):
    def __init__(self):
        """Инициализирует подключение к API при создании экземпляра класса"""
        self._connect()

    @abstractmethod
    def _connect(self):
        """Приватный метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query, per_page=100):
        """Метод для получения данных о вакансиях"""
        pass


class HeadHunterAPI(JobAPI):

    url: str
    headers: dict
    params: dict

    def __init__(self):
        """Инициализирует параметры для подключения и поиска вакансий с помощью API hh.ru"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}
        super().__init__()

    def _connect(self):
        """Приватный метод для подключения к API hh.ru"""
        # Поскольку API hh.ru может возвращать разные результаты в зависимости от параметров,
        # мы не будем просто делать запрос в _connect
        pass

    def get_vacancies(self, search_query, per_page=100):
        """Метод для получения данных о вакансиях с использованием API hh.ru"""
        self.__params["text"] = search_query
        self.__params["per_page"] = per_page

        vacancies = []
        page = 0
        while page < 10:
            self.__params["page"] = page
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                raise ConnectionError(f"Не удалось подключиться к API: {response.status_code}")

            data = response.json()
            vacancies.extend(data.get("items", []))
            if not data.get("items"):
                break  # Прерываем цикл, если нет вакансий на текущей странице
            page += 1

        return json.dumps(vacancies, ensure_ascii=False, indent=4)
