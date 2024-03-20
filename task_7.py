import random
import matplotlib.pyplot as plt



def roll_dice():
    # Функція, що імітує кидок кубика
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    """
    Функція для симуляції кидків двох кубиків та обчислення ймовірностей сум чисел
    методом Монте-Карло.
    
    Args:
        num_rolls (int): Кількість кидків кубиків, які потрібно виконати.
        
    Returns:
        list: Список ймовірностей кожної можливої суми чисел.
    """
    results = [0] * 13  # Масив для збереження кількості випадань кожної суми
    for _ in range(num_rolls):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1
    probabilities = [count / num_rolls * 100 for count in results[2:]]  # Обчислення ймовірностей
    return probabilities

def print_probabilities(probabilities):
    # Виведення ймовірностей кожної суми
    print("Сума | Імовірність")
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i} | {prob:.2f}% ({prob/100:.2f})")

def compare_with_analytical(probabilities):
    #Порівняння отриманих результатів з аналітичними розрахунками
    analytical_probabilities = [
        1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36
    ]
    print("Сума | Імовірність (Монте-Карло) | Імовірність (аналітично)")
    for i, prob in enumerate(probabilities, start=2):
        analytical_prob = analytical_probabilities[i-2] * 100
        print(f"{i} | {prob:.2f}% | {analytical_prob:.2f}%")


def print_results(probabilities, analytical_probabilities):
    # Виведення результатів методу Монте-Карло та порівняння з аналітичними розрахунками
    print("Результати отримані методом Монте-Карло:")
    print("Сума | Імовірність")
    for i, prob in enumerate(probabilities, start=2):
        print(f"{i:<4d} | {prob:.2f}% ({prob/100:.2f})")

    print("\nПорівняння з аналітичними розрахунками:")
    print("Сума | Імовірність (Монте-Карло) | Імовірність (аналітично)")
    for i, prob in enumerate(probabilities, start=2):
        analytical_prob = analytical_probabilities[i-2] * 100
        print(f"{i:<5d}| {prob:>6.2f}%                   | {analytical_prob:.2f}%")


def plot_probabilities(probabilities):
    # Побудова графіку ймовірностей кожної суми
    sums = list(range(2, 13))
    plt.bar(sums, probabilities, color='skyblue')
    plt.title('Ймовірності сум кидків двох кубиків')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()



def main():
    num_rolls = 1000000
    probabilities = simulate_dice_rolls(num_rolls)
    analytical_probabilities = [
        1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36
    ]
    print_results(probabilities, analytical_probabilities)
    plot_probabilities(probabilities)



if __name__ == "__main__":
    main()
