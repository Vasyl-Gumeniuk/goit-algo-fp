def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []

    # Проходимося по відсортованим стравам і обираємо ті, які можна додати до списку обраних
    for item, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            total_cost += data['cost']
            total_calories += data['calories']
            chosen_items.append(item)

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо матрицю для зберігання оптимальних значень
    dp_matrix = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Заповнюємо матрицю значеннями, що відображають найбільшу кількість калорій для кожного бюджету
    for i, (item, data) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if data['cost'] <= j:
                dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i-1][j - data['cost']] + data['calories'])
            else:
                dp_matrix[i][j] = dp_matrix[i-1][j]

    # Відновлюємо оптимальний набір страв
    chosen_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp_matrix[i][j] != dp_matrix[i-1][j]:
            chosen_items.append(list(items.keys())[i-1])
            j -= items[list(items.keys())[i-1]]['cost']
        i -= 1

    # Повертаємо набір страв та загальну кількість калорій
    total_calories = dp_matrix[len(items)][budget]
    return chosen_items, total_calories


def main():
    # Приклад використання
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    # Викликаємо жадібний алгоритм та виводимо результат
    chosen_items, total_calories = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print("Обрані страви:", chosen_items)
    print("Загальна кількість калорій:", total_calories)

    # Викликаємо алгоритм динамічного програмування та виводимо результат
    chosen_items, total_calories = dynamic_programming(items, budget)
    print("\nДинамічне програмування:")
    print("Обрані страви:", chosen_items)
    print("Загальна кількість калорій:", total_calories)


if __name__=="__main__":
    main()
