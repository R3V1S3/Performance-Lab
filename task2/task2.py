import sys

def read_circle_data(filename):
    with open(filename, 'r') as file:
        # Первая строка содержит координаты центра окружности
        x, y = map(float, file.readline().split())
        # Вторая строка содержит радиус
        r = float(file.readline().strip())
    return (x, y, r)

def read_dot_data(filename):
    with open(filename, 'r') as file:
        dots = []
        for line in file:
            # Считываем координаты точки
            dots.append(tuple(map(float, line.split())))
    return dots

def determine_position(circle, dot):
    x_center, y_center, radius = circle
    x_dot, y_dot = dot
    
    # Вычисляем квадрат расстояния от точки до центра окружности
    distance_squared = (x_dot - x_center) ** 2 + (y_dot - y_center) ** 2
    radius_squared = radius ** 2
    
    if distance_squared == radius_squared:
        return 0  # точка лежит на окружности
    elif distance_squared < radius_squared:
        return 1  # точка внутри
    else:
        return 2  # точка снаружи

if __name__ == "__main__":
    # Проверяем, что переданы необходимые аргументы
    if len(sys.argv) != 3:
        print("Пример использования: python task2.py circle.txt dot.txt")
        sys.exit(1)
    
    circle_file = sys.argv[1]
    dot_file = sys.argv[2]
    
    # Считываем данные из файлов
    circle = read_circle_data(circle_file)
    dots = read_dot_data(dot_file)
    
    # Определяем и выводим положение каждой точки
    for dot in dots:
        position = determine_position(circle, dot)
        print(position)
