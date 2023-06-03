# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6)

def print_operation_table(operation, num_rows=6, num_columns=6):
    # Проход по строкам.
    for i in range(1, num_rows + 1):
        # Проход по столбцам.
        for j in range(1, num_columns + 1):
            # Вывод данных.
            print(operation(i, j), end="\t")
        print()


# Функция lambda = operations.
print_operation_table(lambda x, y: x * y)
