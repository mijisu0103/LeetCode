import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda emp: emp['salary'] if emp['employee_id'] % 2 == 1 and emp['name'][0] != 'M' else 0, axis=1)
    employees = employees.sort_values('employee_id')
    return employees[['employee_id', 'bonus']]