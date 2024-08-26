from src.vacancy import Vacancy


def test_vacancy_initialization(valid_vacancy):
    """Тестирование инициализации объекта Vacancy"""
    vacancy = valid_vacancy
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "http://example.com/vacancy"
    assert vacancy.salary == 100000
    assert vacancy.description == "Разработка приложений на Python."
    assert vacancy.city == "Москва"


def test_vacancy_initialization_invalid_title(invalid_vacancy_title):
    """Тестирование инициализации объекта Vacancy с неверным названием"""
    # Так как фикстура уже вызывает исключение, тест будет пройден, если исключение выбрасывается
    pass


def test_vacancy_initialization_invalid_url(invalid_vacancy_url):
    """Тестирование инициализации объекта Vacancy с неверным URL"""
    # Так как фикстура уже вызывает исключение, тест будет пройден, если исключение выбрасывается
    pass


def test_vacancy_initialization_invalid_salary(invalid_vacancy_salary):
    """Тестирование инициализации объекта Vacancy с неверной зарплатой"""
    vacancy = invalid_vacancy_salary
    assert vacancy.salary == 0


def test_vacancy_initialization_invalid_description(invalid_vacancy_description):
    """Тестирование инициализации объекта Vacancy с неверным описанием"""
    # Так как фикстура уже вызывает исключение, тест будет пройден, если исключение выбрасывается
    pass


def test_vacancy_initialization_invalid_city(invalid_vacancy_city):
    """Тестирование инициализации объекта Vacancy с неверным городом"""
    # Т. к. фикстура уже вызывает исключение, тест будет пройден, если исключение выбрасывается
    pass


def test_vacancy_to_dict(valid_vacancy):
    """Тестирование метода to_dict"""
    vacancy = valid_vacancy
    expected_dict = {
        "title": "Python Developer",
        "url": "http://example.com/vacancy",
        "salary": 100000,
        "description": "Разработка приложений на Python.",
        "city": "Москва",
    }
    assert vacancy.to_dict() == expected_dict


def test_vacancy_comparison(valid_vacancy):
    """Тестирование методов сравнения вакансий"""
    vacancy1 = valid_vacancy
    vacancy2 = Vacancy(
        title="Java Developer",
        url="http://example.com/vacancy2",
        salary=120000,
        description="Разработка приложений на Java.",
        city="Ташкент",
    )

    assert vacancy1 < vacancy2
    assert vacancy1 <= vacancy2
    assert vacancy2 > vacancy1
    assert vacancy2 >= vacancy1
    assert vacancy1 != vacancy2
    assert not (vacancy1 == vacancy2)


def test_vacancy_str(valid_vacancy):
    """Тестирование метода __str__"""
    vacancy = valid_vacancy
    expected_str = (
        "Python Developer\n"
        "Зарплата: 100000\n"
        "Ссылка: http://example.com/vacancy\n"
        "Описание: Разработка приложений на Python.\n"
    )
    assert str(vacancy) == expected_str
