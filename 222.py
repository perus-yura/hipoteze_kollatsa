import networkx as nx
import matplotlib.pyplot as plt

def get_collatz_path(n):
    path = []
    curr = n
    while curr != 1:
        path.append(curr)
        curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
    path.append(1)
    return path[::-1]

def visualize_fast_path(target):
    path = get_collatz_path(target)
    G = nx.DiGraph()
    
    # Створюємо ребра та типи зв'язків
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        G.add_edge(u, v, type='2n' if v == u * 2 else 'odd')

    # Налаштування розміру вікна залежно від довжини шляху
    plt.figure(figsize=(16, 6))
    
    # Використовуємо лінійний лейаут, щоб шлях не плутався
    pos = nx.shell_layout(G) 
    
    # Малюємо вузли
    node_colors = ['#FFD700' if n == 1 else ('#90EE90' if n == target else '#ADD8E6') for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color=node_colors, edgecolors='black')
    
    # Малюємо підписи
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    # Малюємо ребра окремо за типами
    e_2n = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == '2n']
    e_odd = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'odd']
    
    nx.draw_networkx_edges(G, pos, edgelist=e_2n, width=1.5, edge_color='blue', arrowsize=15)
    nx.draw_networkx_edges(G, pos, edgelist=e_odd, width=2, edge_color='red', style='dashed', arrowsize=15)

    plt.title(f"Генетичний шлях числа {target} від Одиниці", fontsize=14)
    plt.axis('off')
    print(f"Успішно знайдено шлях довжиною {len(path)} кроків.")
    plt.show()

if __name__ == "__main__":
    # Запускаємо для 27
    visualize_fast_path(31)