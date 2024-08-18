from src.interaction_with_files import JSONFileHandler
import pytest
import os
import json


@pytest.fixture
def temp_file():
    """Фикстура для создания и удаления временного файла для тестов"""
    directory = os.path.join(os.getcwd(), "data")
    filename = "temp_vacancies.json"
    file_path = os.path.join(directory, filename)

    if not os.path.exists(directory):
        os.makedirs(directory)

    if os.path.exists(file_path):
        os.remove(file_path)

    yield file_path

    if os.path.exists(file_path):
        os.remove(file_path)


def test_add_vacancy(temp_file):
    """Тестирование метода add_vacancy"""
    handler = JSONFileHandler(filename=temp_file)
    vacancy = {"title": "Python Developer", "salary": "100000"}

    handler.add_vacancy(vacancy)

    with open(temp_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0] == vacancy


def test_get_vacancies(temp_file):
    """Тестирование метода get_vacancies"""
    handler = JSONFileHandler(filename=temp_file)
    vacancies = [
        {"title": "Python Developer", "salary": "100000"},
        {"title": "Java Developer", "salary": "120000"}
    ]

    for vacancy in vacancies:
        handler.add_vacancy(vacancy)

    result = handler.get_vacancies({"title": "Python Developer"})
    assert len(result) == 1
    assert result[0]["title"] == "Python Developer"


def test_delete_vacancy(temp_file):
    """Тестирование метода delete_vacancy"""
    handler = JSONFileHandler(filename=temp_file)
    vacancy = {"title": "Python Developer", "salary": "100000"}

    handler.add_vacancy(vacancy)
    handler.delete_vacancy(vacancy)

    with open(temp_file, "r", encoding="utf-8") as file:
        data = json.load(file)
        assert len(data) == 0

