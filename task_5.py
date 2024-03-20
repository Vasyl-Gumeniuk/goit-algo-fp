import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає ребра до графу для вузлів дерева та обчислює позиції вузлів для візуалізації.
    :param graph: Об'єкт графу NetworkX.
    :param node: Поточний вузол.
    :param pos: Словник з позиціями вузлів.
    :param x: Поточне значення координати X.
    :param y: Поточне значення координати Y.
    :param layer: Поточний шар в дереві.
    :return: Об'єкт графу NetworkX з доданими ребрами.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def update_colors(graph, colors):
    """
    Оновлює кольори вузлів у графі.
    :param graph: Об'єкт графу NetworkX.
    :param colors: Словник з кольорами вузлів.
    """
    for node_id, node_color in colors.items():
        graph.nodes[node_id]['color'] = node_color

def animate(frame):
    """
    Функція анімації для оновлення кольорів вузлів та відображення графу.
    :param frame: Поточна кадр анімації.
    """
    update_colors(tree, frames[frame])
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

def dfs(node, visited=None):
    """
    Обхід у глибину для визначення кольорів вузлів.
    :param node: Поточний вузол.
    :param visited: Множина відвіданих вузлів.
    """
    if visited is None:
        visited = set()
    visited.add(node)
    node.color = "#%02x%02x%02x" % (200 - len(visited) * 10, 200 - len(visited) * 10, 255)
    frames.append({node.id: node.color})
    if node.left and node.left not in visited:
        dfs(node.left, visited)
    if node.right and node.right not in visited:
        dfs(node.right, visited)

def bfs(node):
    """
    Обхід у ширину для визначення кольорів вузлів.
    :param node: Початковий вузол.
    """
    queue = [node]
    visited = set()
    visited.add(node)
    while queue:
        current_node = queue.pop(0)
        current_node.color = "#%02x%02x%02x" % (200 - len(visited) * 10, 200 - len(visited) * 10, 255)
        frames.append({current_node.id: current_node.color})
        if current_node.left and current_node.left not in visited:
            queue.append(current_node.left)
            visited.add(current_node.left)
        if current_node.right and current_node.right not in visited:
            queue.append(current_node.right)
            visited.add(current_node.right)

def main():
    global tree, pos, labels, frames

    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Підготовка до візуалізації
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    frames = []

    choice = input("Оберіть обхід для візуалізації (DFS або BFS): ").upper()
    while choice not in ["DFS", "BFS"]:
        print("Введення не коректне. Оберіть між DFS або BFS.")
        choice = input("Оберіть обхід для візуалізації (DFS або BFS): ").upper()

    if choice == "DFS":
        dfs(root)
    elif choice == "BFS":
        bfs(root)

    # Створення анімації
    fig, ax = plt.subplots(figsize=(8, 5))
    ani = FuncAnimation(fig, animate, frames=len(frames), interval=1000, repeat=True)  # Повторювати анімацію безкінечно

    plt.show()



if __name__ == "__main__":
    main()