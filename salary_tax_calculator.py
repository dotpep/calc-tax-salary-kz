from typing import Tuple


def calculate_tax_components(salary: int) -> Tuple[float, float, float, float, float, float, float, float]:
    """Рассчитать различные налоговые компоненты на основе заданной зарплаты."""
    basic_mrp: float = 14 * 3450  # 14МРП (Месячный расчётный показатель)

    # ОПВ (Обязательные пенсионные взносы)
    pension_contributions: float = (salary * 10) / 100

    # ВОСМС (Взносы на обязательное социальное медицинское страхование)
    social_insurance_contributions: float = (salary * 2) / 100

    # ИПН (Индивидуальный подоходный налог)
    income_tax: float = ((salary - pension_contributions - basic_mrp - social_insurance_contributions) * 10) / 100

    # CO (Социальные отчисления)
    social_contributions: float = ((salary - pension_contributions) * 3.5) / 100

    # СН (Социальный налог)
    tax_social: float = ((salary - pension_contributions - social_insurance_contributions) * 9.5) / 100

    # ОСМС (Отчисления на обязательное социальное медицинское страхование)
    medical_insurance_contributions: float = (salary * 3) / 100

    # Расчет зарплаты с налогами на руку
    on_hands_salary: float = salary - pension_contributions - social_insurance_contributions - income_tax

    return basic_mrp, pension_contributions, social_insurance_contributions, \
        income_tax, social_contributions, tax_social, \
        medical_insurance_contributions, on_hands_salary


def user_salary_input() -> int:
    """Получить данные о зарплате от пользователя и убедится, что это целое положительное число."""
    while True:
        try:
            salary: int = int(input("Ваша зарплата: "))
            if salary > 0:
                return salary
            else:
                print("Invalid input! Зарплата должна быть положительным числом.")
        except ValueError:
            print("Type Error! Напишите сумму (целое число) вашей зарплаты.")


def calculation_information(salary: int, *tax_components: float) -> None:
    """Отображение информации и сведений о рассчитанном налоге."""
    basic_mrp, pension_contributions, social_insurance_contributions, \
        income_tax, social_contributions, tax_social, medical_insurance_contributions, net_salary = tax_components

    print("\n----- Идет вычисление... -----")
    print(f"ОПВ (Обязательные пенсионные взносы): "
          f"\n{salary=} * 10% = {pension_contributions}")
    print(
        f"ВОСМС (Взносы на обязательное социальное медицинское страхование): "
        f"\n{salary=} * 2% = {social_insurance_contributions}")
    print(
        f"ИПН (Индивидуальный подоходный налог): "
        f"\n({salary=} - ОПВ={pension_contributions} - 14МРП={basic_mrp} - ВОСМС={social_insurance_contributions}) * 10% = {income_tax}")
    print("\n----- Вычисление... -----")
    print(f"CO (Социальные отчисления): "
          f"\n({salary=} - ОПВ={pension_contributions}) * 3.5% = {social_contributions}")
    print(
        f"СН (Социальный налог): "
        f"\n({salary=} - ОПВ={pension_contributions} - ВОСМС={social_insurance_contributions}) * 3.5% - CO={social_contributions} = {tax_social}")
    print(
        f"ОСМС (Отчисления на обязательное социальное медицинское страхование): "
        f"\n{salary=} * 3% = {medical_insurance_contributions}")
    print("\n----- На руки: -----")
    print(
        f"Расчет зарплаты с налогами на руки: "
        f"\n{salary=} - ОПВ={pension_contributions} - ВОСМС={social_insurance_contributions} - ИПН={income_tax} = {net_salary}")
    print(f"На руки: {net_salary} тенге\n")


def main() -> None:
    """Основная функция для выполнения программы расчета налога на заработную плату."""
    print("\nЯ могу рассчитать налог для вашей зарплаты в Казахстане!")

    salary: int = user_salary_input()

    tax_components: tuple = calculate_tax_components(salary)
    calculation_information(salary, *tax_components)


if __name__ == "__main__":
    main()
