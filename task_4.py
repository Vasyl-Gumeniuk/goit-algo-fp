import networkx as nx
import matplotlib.pyplot as plt


def visualize_binary_heap(heap):
    # Створюємо порожній граф
    G = nx.Graph()

    def add_nodes(heap, i):
        # Рекурсивно додаємо вузли до графа
        if i < len(heap):
            G.add_node(heap[i])
            add_nodes(heap, 2 * i + 1)  # лівий дочірній вузол
            add_nodes(heap, 2 * i + 2)  # правий дочірній вузол

    add_nodes(heap, 0)

    def add_edges(heap, i):
        # Рекурсивно додаємо зв'язки між вузлами
        if i < len(heap):
            if 2 * i + 1 < len(heap):
                G.add_edge(heap[i], heap[2 * i + 1])  # зв'язок з лівим дочірнім вузлом
            if 2 * i + 2 < len(heap):
                G.add_edge(heap[i], heap[2 * i + 2])  # зв'язок з правим дочірнім вузлом
            add_edges(heap, 2 * i + 1)  # рекурсивний виклик для лівого дочірнього вузла
            add_edges(heap, 2 * i + 2)  # рекурсивний виклик для правого дочірнього вузла

    add_edges(heap, 0)

    pos = {}

    def assign_positions(heap, i, level, xpos):
        # Рекурсивно визначаємо позиції вузлів
        if i < len(heap):
            pos[heap[i]] = (xpos, -level)
            # Визначаємо позиції для лівого та правого дочірнього вузла
            assign_positions(heap, 2 * i + 1, level + 1, xpos - 2 ** (max_levels - level - 1))
            assign_positions(heap, 2 * i + 2, level + 1, xpos + 2 ** (max_levels - level - 1))

    max_levels = len(bin(len(heap))) - 3  # максимальна кількість рівнів у бінарній купі
    assign_positions(heap, 0, 0, 0)

    # Візуалізуємо граф
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10)
    plt.show()


def main():
    # Приклад використання:
    heap = [0, 4, 5, 10, 1, 3]
    visualize_binary_heap(heap)



if __name__ == "__main__":
    main()

