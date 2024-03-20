import turtle



def draw_pifagor_tree(t, length, level):
    """Рекурсивно малюємо фрактал 'дерево Піфагора'."""
    if level == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagor_tree(t, length * 0.6, level - 1)
    t.right(90)
    draw_pifagor_tree(t, length * 0.6, level - 1)
    t.left(45)
    t.backward(length)


def main():
    """Виконуємо основну логіку програми."""
    level = int(input("Введіть рівень рекурсії: "))

    # Ініціалізуємо вікно та turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    # Викликаємо функцію для малювання дерева Піфагора
    draw_pifagor_tree(t, 150, level)

    # Закриваємо вікно при кліку на нього
    screen.exitonclick()



if __name__ == "__main__":
    main()
