import heapq

def dijkstra(graph, start):
    # Ініціалізуємо словник для зберігання найкоротших відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Ініціалізуємо бінарну купу та додаємо початкову вершину з вагою 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань до вершини більша, ніж збережена відстань, ігноруємо її
        if current_distance > distances[current_vertex]:
            continue

        # Оновлюємо відстані до сусідів поточної вершини"""
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    # Створення графа
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5, 'F': 4},
        'C': {'A': 4, 'B': 2, 'D': 1, 'G': 3},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3, 'F': 7},
        'F': {'B': 4, 'E': 7, 'G': 2},
        'G': {'C': 3, 'F': 2}
    }

    # Виклик алгоритму Дейкстри з вершини 'A'
    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)

    # Виведення результатів
    print("Найкоротші відстані від вершини:", start_vertex)
    for vertex, distance in shortest_distances.items():
        if vertex != start_vertex:
            print(f"до вершини {vertex}: {distance}")



if __name__ == "__main__":
    main()
