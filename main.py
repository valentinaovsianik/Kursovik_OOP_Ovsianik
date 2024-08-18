from src.interaction_with_API import HeadHunterAPI
from src.interaction_with_files import JSONFileHandler
from src.utils import get_top_vacancies, print_vacancies, sort_vacancies, get_vacancies_by_salary, filter_vacancies, filter_vacancies_by_city

from src.vacancy import Vacancy


def user_interaction():
    hh_api = HeadHunterAPI()
    print("Добро пожаловать в систему поиска вакансий!")
    search_query = input("Введите запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат. Например, 10000-20000: ")
    city = input("Введите город, в котором ищете вакансии: ")

    try:
        min_salary, max_salary = map(int, salary_range.split("-"))
    except ValueError:
        print("Неверный формат диапазона зарплат. Используйте формат 'минимум-максимум'.")
        return

    hh_vacancies_json = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies_json)
    json_saver = JSONFileHandler()

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy.to_dict())

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_salary, max_salary)
    city_filtered_vacancies = filter_vacancies_by_city(ranged_vacancies, city)
    sorted_vacancies = sort_vacancies(city_filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)


    print(f"Топ {top_n} вакансий по запросу '{search_query}' в городе '{city}':")
    print_vacancies(top_vacancies)
    print("Поиск вакансий завершен.")


if __name__ == "__main__":
    user_interaction()
