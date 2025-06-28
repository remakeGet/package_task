from tabulate import tabulate
from loguru import logger
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
CURRENCY = os.getenv("CURRENCY", "₽")

# База данных сотрудников
EMPLOYEES_DB = {
    1: {"name": "Иван Петров", "position": "Разработчик", "base_salary": 100_000},
    2: {"name": "Анна Сидорова", "position": "Менеджер", "base_salary": 90_000},
    3: {"name": "Сергей Иванов", "position": "Тестировщик", "base_salary": 80_000},
}

def get_employees(employee_id: int = None) -> list | dict:
    """Возвращает данные сотрудников в виде таблицы или конкретного сотрудника."""
    current_date = datetime.now().date()
    
    if employee_id is None:
        logger.info(f"[{current_date}] Запрос списка всех сотрудников")
        table = [
            [emp_id, emp["name"], emp["position"], f"{emp['base_salary']} {CURRENCY}"]
            for emp_id, emp in EMPLOYEES_DB.items()
        ]
        print(tabulate(
            table,
            headers=["ID", "Имя", "Должность", "Оклад"],
            tablefmt="grid"
        ))
        return EMPLOYEES_DB
    
    if employee_id in EMPLOYEES_DB:
        employee = EMPLOYEES_DB[employee_id]
        logger.info(f"[{current_date}] Данные сотрудника ID {employee_id}")
        print(
            f"ID: {employee_id}\n"
            f"Имя: {employee['name']}\n"
            f"Должность: {employee['position']}\n"
            f"Оклад: {employee['base_salary']} {CURRENCY}"
        )
        return employee
    
    logger.error(f"[{current_date}] Сотрудник с ID {employee_id} не найден!")
    return {}

def get_employee_salary(employee_id: int) -> float:
    """Возвращает оклад сотрудника по ID."""
    if employee_id in EMPLOYEES_DB:
        return EMPLOYEES_DB[employee_id]["base_salary"]
    raise ValueError(f"Сотрудник с ID {employee_id} не найден")