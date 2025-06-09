from src.hh_api import HeadHunterAPI
from src.json_handler import JSONHandler
from src.vacancy import Vacancy


def filter_vacancies(vacancies: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""
    if not filter_words:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        vacancy_text = f"{vacancy.title} {vacancy.description} {vacancy.company}".lower()
        if all(word.lower() in vacancy_text for word in filter_words):
            filtered.append(vacancy)
    return filtered


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрация вакансий по диапазону зарплат"""
    if not salary_range.strip():
        return vacancies

    try:
        min_salary, max_salary = map(int, salary_range.split('-'))
    except ValueError:
        print("Некорректный формат диапазона зарплат. Используйте формат: 100000-150000")
        return vacancies

    ranged_vacancies = []
    for vacancy in vacancies:
        vacancy_salary = vacancy.salary_from or vacancy.salary_to or 0
        if min_salary <= vacancy_salary <= max_salary:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def print_vacancies(vacancies: list[Vacancy], top_n: int) -> None:
    """Вывод отфильтрованных вакансий"""
    if not vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    print(f"\nТоп-{top_n} вакансий:")
    for i, vacancy in enumerate(sorted(vacancies, reverse=True)[:top_n], 1):
        salary_from = vacancy.salary_from if vacancy.salary_from is not None else "Не указано"
        salary_to = vacancy.salary_to if vacancy.salary_to is not None else "Не указано"
        print(f"{i}. {vacancy.title} в {vacancy.company}")
        print(f"   Зарплата: {salary_from} - {salary_to}")
        print(f"   Описание: {vacancy.description[:100]}...")
        print(f"   Ссылка: {vacancy.url}\n")


def user_interaction():
    """Функция взаимодействия с пользователем"""
    print("Добро пожаловать в парсер вакансий с HeadHunter!")

    # Получение параметров поиска
    keyword = input("Введите ключевое слово для поиска вакансий: ").strip()
    per_page = int(input("Сколько вакансий загрузить (макс. 100)? ").strip())

    # Получение вакансий
    hh_api = HeadHunterAPI()
    try:
        vacancies_data = hh_api.get_vacancies(keyword, per_page)
        print(f"\nНайдено {len(vacancies_data)} вакансий.")
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    # Сохранение вакансий
    json_handler = JSONHandler()
    json_handler.add_to_file(vacancies_data)
    print("Вакансии сохранены в файл 'vacancies.json'")

    # Преобразование в объекты Vacancy
    vacancies = [Vacancy(**data) for data in vacancies_data]

    # Дополнительные параметры фильтрации
    top_n = int(input("\nВведите количество вакансий для вывода в топ N: ").strip())
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").strip().split()
    salary_range = input("Введите диапазон зарплат (например: 100000-150000): ").strip()

    # Применение фильтров
    filtered_vacancies = filter_vacancies(vacancies, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # Вывод результатов
    print_vacancies(ranged_vacancies, top_n)


if __name__ == "__main__":
    user_interaction()
