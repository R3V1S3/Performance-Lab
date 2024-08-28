import sys

def calculate_minimum_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]  # Находим медиану
    moves = sum(abs(num - median) for num in nums)  # Суммируем шаги для приведения всех чисел к медиане
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пример использования: python task4.py numbers.txt")
        sys.exit(1)
    
    numbers_file = sys.argv[1]
    
    # Считываем числа из файла
    with open(numbers_file, 'r') as file:
        nums = [int(line.strip()) for line in file]
    
    # Вычисляем минимальное количество ходов
    result = calculate_minimum_moves(nums)
    
    # Выводим результат
    print(result)
