import json
from typing import List


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ["_title", "_url", "_salary", "_description", "_city"]

    def __init__(self, title: str, url: str, salary: float, description: str, city: str):
        """Инициализация объекта вакансии с проверкой данных"""
        self._title = self._validate_title(title)
        self._url = self._validate_url(url)
        self._salary = self._validate_salary(salary)
        self._description = self._validate_description(description)
        self._city = self._validate_city(city)

    @staticmethod
    def cast_to_object_list(vacancies_json: str) -> List['Vacancy']:
        """Создает список объектов Vacancy из JSON-строки"""
        vacancies_data = json.loads(vacancies_json)
        vacancies_list = []

        for item in vacancies_data:
            try:
                # Извлечение и проверка данных
                title = item.get("name", "")
                url = item.get("alternate_url", "")
                salary_info = item.get("salary", {})
                salary_from = salary_info.get("from") if isinstance(salary_info, dict) else None
                salary = salary_from if salary_from is not None else 0

                description_info = item.get("snippet", {})
                description = description_info.get("responsibility", "") if isinstance(description_info, dict) else ""

                area_info = item.get("area", {})
                city = area_info.get("name", "") if isinstance(area_info, dict) else ""

                # Проверка валидности полей перед созданием объекта
                if title and url and isinstance(salary, (int, float)) and description is not None and city:
                    vacancy = Vacancy(title, url, salary, description, city)
                    vacancies_list.append(vacancy)

            except ValueError as e:
                print(f"Ошибка при создании вакансии: {e}, данные: {item}")

        return vacancies_list

    def to_dict(self) -> dict:
        """Преобразует объект Vacancy в словарь."""
        return {"title": self._title, "url": self._url, "salary": self._salary, "description": self._description, "city": self._city}

    def _validate_title(self, title: str) -> str:
        """Проверяет корректность названия вакансии"""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название вакансии должно быть не пустой строкой.")
        return title

    def _validate_url(self, url: str) -> str:
        """Проверяет корректность URL"""
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("URL должен быть строкой, начинающейся с 'http'.")
        return url

    def _validate_salary(self, salary: float) -> float:
        """Проверяет корректность зарплаты"""
        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def _validate_description(self, description: str) -> str:
        """Проверяет корректность описания вакансии"""
        if not isinstance(description, str):
            raise ValueError("Описание вакансии должно быть строкой.")
        return description

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.url}\nОписание: {self.description}\n"

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (меньше)"""
        return self._salary < other._salary

    def __le__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (меньше или равно)"""
        return self._salary <= other._salary

    def __eq__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (равно)"""
        return self._salary == other._salary

    def __ne__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (не равно)"""
        return self._salary != other._salary

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (больше)"""
        return self._salary > other._salary

    def __ge__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (больше или равно)"""
        return self._salary >= other._salary

    @property
    def title(self) -> str:
        """Возвращает название вакансии"""
        return self._title

    @property
    def url(self) -> str:
        """Возвращает URL вакансии"""
        return self._url

    @property
    def salary(self) -> float:
        """Возвращает зарплату вакансии"""
        return self._salary

    @property
    def description(self) -> str:
        """Возвращает описание вакансии"""
        return self._description

    def _validate_city(self, city: str) -> str:
        """Проверяет корректность названия города"""
        if not isinstance(city, str) or not city.strip():
            raise ValueError("Название города должно быть не пустой строкой.")
        return city

    @property
    def city(self) -> str:
        """Возвращает город вакансии"""
        return self._city
