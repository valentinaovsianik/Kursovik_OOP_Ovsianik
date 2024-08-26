from src.utils import (
    filter_vacancies,
    filter_vacancies_by_city,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)


def test_filter_vacancies(vacancies):
    """Тестирование функции filter_vacancies"""
    keywords = ["python", "специалист"]
    filtered = filter_vacancies(vacancies, keywords)

    for vacancy in filtered:
        print(f"Вакансия: {vacancy.title}, описание: {vacancy.description}")

    assert len(filtered) == 2
    assert any(vacancy.title == "Python Developer" for vacancy in filtered)
    assert any(vacancy.title == "Специалист по обработке данных" for vacancy in filtered)


def test_get_vacancies_by_salary(vacancies):
    """Тестирование функции get_vacancies_by_salary"""
    min_salary = 95000
    max_salary = 120000
    filtered = get_vacancies_by_salary(vacancies, min_salary, max_salary)
    assert len(filtered) == 3
    assert any(vacancy.salary == 100000 for vacancy in filtered)
    assert any(vacancy.salary == 120000 for vacancy in filtered)
    assert any(vacancy.salary == 95000 for vacancy in filtered)


def test_sort_vacancies(vacancies):
    """Тестирование функции sort_vacancies"""
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0].salary == 120000
    assert sorted_vacancies[1].salary == 100000
    assert sorted_vacancies[2].salary == 95000
    assert sorted_vacancies[3].salary == 90000


def test_get_top_vacancies(vacancies):
    """Тестирование функции get_top_vacancies"""
    sorted_vacancies = sort_vacancies(vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].salary == 120000
    assert top_vacancies[1].salary == 100000


def test_filter_vacancies_by_city(vacancies):
    """Тестирование функции filter_vacancies_by_city"""
    city = "Саратов"
    filtered = filter_vacancies_by_city(vacancies, city)
    assert len(filtered) == 1
    assert all(vacancy.city == "Саратов" for vacancy in filtered)


def test_print_vacancies(capsys, vacancies):
    """Тестирование функции print_vacancies"""
    print_vacancies(vacancies)
    captured = capsys.readouterr().out.splitlines()
    assert len(captured) == 4
    assert captured[0] == "Вакансия: Python Developer, зарплата: 100000, ссылка: http://example.com/vacancy1"
    assert captured[1] == "Вакансия: Java Developer, зарплата: 120000, ссылка: http://example.com/vacancy2"
    assert (
        captured[2] == "Вакансия: Специалист по обработке данных, зарплата: 95000, ссылка: http://example.com/vacancy3"
    )
    assert captured[3] == "Вакансия: Frontend Developer, зарплата: 90000, ссылка: http://example.com/vacancy4"
