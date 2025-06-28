from application.salary import calculate_salary
from application.db.people import get_employees
from loguru import logger
from datetime import datetime

if __name__ == '__main__':
    logger.info(f"\n=== Бухгалтерия {datetime.now().date()} ===")
    
    # Пример использования
    get_employees()          # Список всех
    print("\n" + "-"*40 + "\n")
    get_employees(2)        # Конкретный сотрудник
    print("\n" + "-"*40 + "\n")
    calculate_salary(employee_id=2, bonus=15_000)  # Расчёт с премией