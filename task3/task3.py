import json
import sys

def fill_values(tests, values_dict):
    # Проходим по каждому тесту в списке
    for test in tests:
        test_id = test["id"]
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        if "values" in test:
            fill_values(test["values"], values_dict)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Пример использования: python task3.py values.json tests.json report.json")
        sys.exit(1)
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Чтение файла values.json
    with open(values_file, 'r') as f:
        values_data = json.load(f)
    
    # Преобразуем список значений в словарь для быстрого поиска по id
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Чтение файла tests.json
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    # Заполняем значения
    fill_values(tests_data["tests"], values_dict)

    # Запись результата в report.json
    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=4)

    print("Отчет сформирован и записан в", report_file)
