from loguru import logger
from datetime import datetime
from dotenv import load_dotenv
import os
from application.db.people import get_employee_salary

load_dotenv()
TAX_RATE = float(os.getenv("TAX_RATE", 0.13))
CURRENCY = os.getenv("CURRENCY", "₽")

def calculate_salary(employee_id: int, bonus: float = 0) -> float:
    """Рассчитывает зарплату после вычета налога."""
    current_date = datetime.now().date()
    base_salary = get_employee_salary(employee_id)
    tax = (base_salary + bonus) * TAX_RATE
    net_salary = base_salary + bonus - tax
    
    logger.info(f"[{current_date}] Расчёт зарплаты для ID {employee_id}")
    print(
        f"Оклад: {base_salary} {CURRENCY}\n"
        f"Премия: {bonus} {CURRENCY}\n"
        f"Налог ({TAX_RATE*100}%): {tax:.2f} {CURRENCY}\n"
        f"Итого на руки: {net_salary:.2f} {CURRENCY}"
    )
    return net_salary