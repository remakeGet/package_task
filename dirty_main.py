from application.salary import *
from application.db.people import *
from loguru import logger
from datetime import datetime

if __name__ == '__main__':
    logger.warning("=== Запуск через 'грязный' импорт ===")
    calculate_salary(employee_id=3, bonus=5_000)
    print("\n" + "-"*40 + "\n")
    get_employees(3)