from unittest.mock import patch

import pytest

from src.interaction_with_API import HeadHunterAPI


@patch("requests.get")
def test_get_vacancies_success(mock_get):
    """Тестируем успешное получение вакансий"""

    # Настраиваем мок для возврата тестовых данных
    mock_response = {
        "items": [
            {
                "id": "1",
                "name": "Python Developer",
                "url": "https://hh.ru/vacancy/1",
                "salary": {"from": 100000, "to": 150000},
                "snippet": {"responsibility": "Developing in Python"},
            }
        ]
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    hh_api = HeadHunterAPI()
    search_query = "Python"
    vacancies_json = hh_api.get_vacancies(search_query)

    assert '"name": "Python Developer"' in vacancies_json
    assert '"id": "1"' in vacancies_json
    assert '"url": "https://hh.ru/vacancy/1"' in vacancies_json


@patch("requests.get")
def test_get_vacancies_no_results(mock_get):
    """Тестируем случай, когда по запросу нет вакансий"""

    mock_response = {"items": []}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    hh_api = HeadHunterAPI()
    search_query = "NonExistentJobTitle"
    vacancies_json = hh_api.get_vacancies(search_query)

    assert vacancies_json == "[]"


@patch("requests.get")
def test_get_vacancies_api_error(mock_get):
    """Тестируем ошибку подключения к API"""

    mock_get.return_value.status_code = 500

    hh_api = HeadHunterAPI()
    search_query = "Python"

    with pytest.raises(ConnectionError, match="Не удалось подключиться к API: 500"):
        hh_api.get_vacancies(search_query)
