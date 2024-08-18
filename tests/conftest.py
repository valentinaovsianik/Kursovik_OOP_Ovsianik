import pytest
from src.vacancy import Vacancy

@pytest.fixture
def valid_vacancy():
    """Фикстура для создания корректного объекта Vacancy"""
    return Vacancy(
        title="Python Developer",
        url="http://example.com/vacancy",
        salary=100000,
        description="Разработка приложений на Python.",
        city="Москва"
    )

@pytest.fixture
def invalid_vacancy_title():
    """Фикстура для создания объекта Vacancy с некорректным названием"""
    with pytest.raises(ValueError):
        return Vacancy(
            title="",
            url="http://example.com/vacancy",
            salary=100000,
            description="Разработка приложений на Python.",
            city="Москва"
        )

@pytest.fixture
def invalid_vacancy_url():
    """Фикстура для создания объекта Vacancy с некорректным URL"""
    with pytest.raises(ValueError):
        return Vacancy(
            title="Python Developer",
            url="invalid_url",
            salary=100000,
            description="Разработка приложений на Python.",
            city="Москва"
        )

@pytest.fixture
def invalid_vacancy_salary():
    """Фикстура для создания объекта Vacancy с некорректной зарплатой"""
    return Vacancy(
        title="Python Developer",
        url="http://example.com/vacancy",
        salary=-100000,
        description="Разработка приложений на Python.",
        city="Москва"
    )

@pytest.fixture
def invalid_vacancy_description():
    """Фикстура для создания объекта Vacancy с некорректным описанием"""
    with pytest.raises(ValueError):
        return Vacancy(
            title="Python Developer",
            url="http://example.com/vacancy",
            salary=100000,
            description=12345,
            city="Москва"
        )

@pytest.fixture
def invalid_vacancy_city():
    """Фикстура для создания объекта Vacancy с некорректным городом"""
    with pytest.raises(ValueError):
        return Vacancy(
            title="Python Developer",
            url="http://example.com/vacancy",
            salary=100000,
            description="Разработка приложений на Python.",
            city=""
        )

@pytest.fixture
def vacancies():
    """Фикстура для создания списка вакансий"""
    return [
        Vacancy(
            title="Python Developer",
            url="http://example.com/vacancy1",
            salary=100000,
            description="Разработка приложений на Python. Работа с Python.",
            city="Минск"
        ),
        Vacancy(
            title="Java Developer",
            url="http://example.com/vacancy2",
            salary=120000,
            description="Разработка приложений на Java.",
            city="Москва"
        ),
        Vacancy(
            title="Специалист по обработке данных",
            url="http://example.com/vacancy3",
            salary=95000,
            description="Анализ данных и построение моделей. Работа специалистом.",
            city="Саратов"
        ),
        Vacancy(
            title="Frontend Developer",
            url="http://example.com/vacancy4",
            salary=90000,
            description="Работа над фронтенд-технологиями.",
            city="Ростов"
        )
    ]
