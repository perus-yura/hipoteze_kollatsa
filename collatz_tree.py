import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def visualize_collatz_tree_ascending(target, max_nodes=40):
    """
    Будує висхідне дерево Коллатца від 1 до цільового числа та візуалізує його.
    """
    if target == 1:
        print("Число 1 є коренем дерева.")
        return

    # Ініціалізація графа
    G = nx.DiGraph()
    G.add_node(1, label='1 (Root)')
    
    # Черга для BFS (пошук в ширину): (поточне число, шлях до нього)
    queue = deque([(1, [1])])
    visited = {1}
    target_path = None

    print(f"--- Побудова висхідного дерева для числа {target} ---")

    nodes_count = 1
    # Обмежуємо кількість вузлів, щоб графік не перетворився на "кашу"
    while queue and nodes_count < max_nodes:
        current, path = queue.popleft()

        # Генеруємо наступні можливі "висхідні" кроки за алгоритмом Калюжного
        next_steps = []
        
        # 1. Основний шлях: множення на 2 (набір токенів)
        next_steps.append(current * 2)
        
        # 2. Інфляційний шлях: (n-1)/3 (якщо результат непарний і > 1)
        if (current - 1) % 3 == 0:
            potential_odd = (current - 1) // 3
            if potential_odd > 1 and potential_odd % 2 != 0:
                next_steps.append(potential_odd)

        for step in next_steps:
            if step not in visited:
                visited.add(step)
                nodes_count += 1
                
                # Додаємо зв'язок у граф
                G.add_edge(current, step)
                
                # Позначаємо тип зв'язку для кольору ліній
                if step == current * 2:
                    G[current][step]['type'] = '2n'
                else:
                    G[current][step]['type'] = 'odd'

                new_path = path + [step]
                if step == target:
                    target_path = new_path
                
                if nodes_count < max_nodes:
                    queue.append((step, new_path))

    # --- Візуалізація ---
    plt.figure(figsize=(14, 10))
    
    # Використовуємо автоматичний розподіл вузлів (spring layout)
    # k регулює відстань між вузлами, щоб вони не накладалися
    pos = nx.spring_layout(G, k=1.5, seed=42)

    # Визначаємо кольори та розміри вузлів
    node_colors = []
    node_sizes = []
    for node in G.nodes():
        if node == 1:
            node_colors.append('#FFD700')  # Золотий для кореня
            node_sizes.append(2000)
        elif node == target:
            node_colors.append('#90EE90')  # Світло-зелений для цілі
            node_sizes.append(2000)
        else:
            node_colors.append('#ADD8E6')  # Блакитний для інших
            node_sizes.append(1000)

    # Малюємо вузли
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')
    
    # Малюємо підписи чисел
    nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold', font_family='sans-serif')

    # Розділяємо ребра за типами для різного стилю малювання
    edges_2n = [(u, v) for u, v, d in G.edges(data=True) if d.get('type') == '2n']
    edges_odd = [(u, v) for u, v, d in G.edges(data=True) if d.get('type') == 'odd']
    
    # Малюємо основні шляхи (сині)
    nx.draw_networkx_edges(G, pos, edgelist=edges_2n, width=1.5, edge_color='blue', style='solid', arrowsize=20)
    
    # Малюємо інфляційні шляхи (червоні пунктирні)
    nx.draw_networkx_edges(G, pos, edgelist=edges_odd, width=2.5, edge_color='red', style='dashed', arrowsize=20)

    # Виділяємо знайдений шлях зеленим кольором
    if target_path:
        print(f"Шлях знайдено: {' -> '.join(map(str, target_path))}")
        path_edges = list(zip(target_path, target_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4.0, edge_color='green', arrowsize=30)

    # Оформлення графіку
    plt.title(f"Висхідне дерево Коллатца: шлях від 1 до {target}", fontsize=18, pad=20)
    plt.axis('off')
    
    # Додаємо легенду для студентів
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='blue', lw=1.5, label='Крок 2n (Токен)'),
        Line2D([0], [0], color='red', lw=2.5, ls='--', label='Крок (n-1)/3 (Інфляція)'),
        Line2D([0], [0], color='green', lw=4, label=f'Знайдений шлях до {target}')
    ]
    plt.legend(handles=legend_elements, loc='lower right', fontsize=12)

    plt.tight_layout()
    plt.show()

# --- Налаштування та запуск ---
if __name__ == "__main__":
    # Спробуємо знайти шлях до числа 27 (інфляційний магнат)
    target_to_find = 31
    # max_nodes можна збільшити, щоб побачити більше гілок дерева
    visualize_collatz_tree_ascending(target_to_find, max_nodes=50)