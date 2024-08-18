def filter_vacancies(vacancies, keywords):
    """Фильтрует вакансии по ключевым словам"""
    return [vacancy for vacancy in vacancies if any(word.lower() in vacancy.description.lower() for word in keywords)]


def get_vacancies_by_salary(vacancies, min_salary, max_salary):
    """Возвращает вакансии с зарплатой в указанном диапазоне (включительно)"""
    return [vacancy for vacancy in vacancies if min_salary <= vacancy.salary <= max_salary]


def sort_vacancies(vacancies):
    """Сортирует вакансии по зарплате в порядке убывания"""
    return sorted(vacancies, key=lambda x: x.salary, reverse=True)


def get_top_vacancies(vacancies, n):
    """Возвращает топ N вакансий по зарплате"""
    return vacancies[:n]


def filter_vacancies_by_city(vacancies, city):
    """Фильтрует вакансии по городу"""
    city = city.lower()
    return [vacancy for vacancy in vacancies if vacancy.city.lower() == city]

def print_vacancies(vacancies):
    """Выводит вакансии в читаемом виде"""
    for vacancy in vacancies:
        print(f"Вакансия: {vacancy.title}, зарплата: {vacancy.salary}, ссылка: {vacancy.url}")
