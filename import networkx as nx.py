import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def visualize_collatz_tree_ascending(target, max_nodes=50):
    if target == 1:
        print("Число 1 є коренем дерева.")
        return

    # Ініціалізація графа
    G = nx.DiGraph()
    G.add_node(1, label='1 (Root)')
    
    # Черга для BFS (число, поточний шлях)
    queue = deque([(1, [1])])
    visited = {1}
    target_path = None

    print(f"--- Побудова та візуалізація висхідного дерева для {target} ---")

    nodes_count = 1
    while queue and nodes_count < max_nodes:
        current, path = queue.popleft()

        # Генеруємо наступні можливі "висхідні" кроки
        next_steps = []
        
        # 1. Завжди можна помножити на 2 (Rule 2n)
        next_steps.append(current * 2)
        
        # 2. Перевіряємо можливість непарного кроку (n-1)/3
        if (current - 1) % 3 == 0:
            potential_odd = (current - 1) // 3
            if potential_odd > 1 and potential_odd % 2 != 0:
                next_steps.append(potential_odd)

        for step in next_steps:
            if step not in visited:
                visited.add(step)
                nodes_count += 1
                
                # Додаємо ребро в граф (від батька до сина у висхідному сенсі)
                G.add_edge(current, step)
                
                # Позначаємо тип кроку для візуалізації
                if step == current * 2:
                    G[current][step]['type'] = '2n'
                else:
                    G[current][step]['type'] = '(n-1)/3'

                new_path = path + [step]
                if step == target:
                    target_path = new_path
                    # Ми знайшли ціль, але продовжуємо BFS трохи далі для краси графа
                
                if nodes_count < max_nodes:
                    queue.append((step, new_path))

    # --- Візуалізація ---
    plt.figure(figsize=(12, 10))
    
    # Використовуємо ієрархічний лейаут для дерев
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot') # Потребує Graphviz
    except ImportError:
        # Якщо Graphviz немає, використовуємо стандартний пружинний лейаут
        print("Graphviz не знайдено, використовується spring_layout (може бути менш наочно).")
        pos = nx.spring_layout(G, seed=42)

    # Малюємо вузли
    node_colors = ['#FFD700' if n == 1 else ('#90EE90' if n == target else '#ADD8E6') for n in G.nodes()]
    node_sizes = [1500 if n == 1 or n == target else 800 for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
    
    # Малюємо мітки вузлів
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Малюємо ребра
    edges_2n = [(u, v) for u, v, d in G.edges(data=True) if d.get('type') == '2n']
    edges_odd = [(u, v) for u, v, d in G.edges(data=True) if d.get('type') == '(n-1)/3']
    
    nx.draw_networkx_edges(G, pos, edgelist=edges_2n, edgewidth=1.5, edge_color='blue', style='solid', arrowsize=20)
    nx.draw_networkx_edges(G, pos, edgelist=edges_odd, edgewidth=2, edge_color='red', style='dashed', arrowsize=20)

    # Виділяємо знайдений шлях
    if target_path:
        print(f"Шлях до {target} знайдено: {' -> '.join(map(str, target_path))}")
        path_edges = list(zip(target_path, target_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edgewidth=3, edge_color='green', arrowsize=25)

    # Налаштування відображення
    plt.title(f"Висхідне дерево Коллатца від 1 (локально навколо {target})", fontsize=16)
    plt.axis('off')
    
    # Додаємо легенду
    blue_line = plt.Line2D([0], [0], color='blue', linestyle='-', linewidth=1.5)
    red_line = plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2)
    green_line = plt.Line2D([0], [0], color='green', linestyle='-', linewidth=3)
    plt.legend([blue_line, red_line, green_line], ['Крок 2n (Токен)', 'Крок (n-1)/3 (Інфляція)', f'Шлях до {target}'], loc='lower right')

    plt.tight_layout()
    plt.show()

# --- Використання ---
# Примітка: Для роботи ієрархічного лейауту `nx_agraph.graphviz_layout` 
# потрібно встановити бібліотеку `pygraphviz` та сам інструмент `Graphviz`.
# Якщо їх немає, код використає стандартний лейаут.

target_number = 27 # Можна ввести будь-яке число
visualize_collatz_tree_ascending(target_number, max_nodes=40)