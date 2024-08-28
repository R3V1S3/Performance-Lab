import sys

def circular_path(n, m):
    # Создаем круговой массив от 1 до n
    arr = list(range(1, n + 1))
    path = []
    
    current_position = 0
    
    while True:
        # Добавляем начальный элемент интервала в путь
        path.append(arr[current_position])
        
        # Рассчитываем новую позицию
        current_position = (current_position + m - 1) % n # Рассчет остатка от деления на n для исключения выхода за пределы массива
        
        if current_position == 0:
            break
    
    return path

if __name__ == "__main__":
    # Получаем аргументы командной строки
    if len(sys.argv) != 3:
        print("Пример использования: python task1.py n m")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    # Получаем путь по круговому массиву
    result = circular_path(n, m)
    
    # Выводим результат в виде строки в консоль
    print(''.join(map(str, result)))
