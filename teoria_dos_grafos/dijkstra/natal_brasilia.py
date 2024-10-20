import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados para o gráfico de cidades brasileiras com distâncias reais aproximadas
graph = [
    ('Natal', 'João Pessoa', 185),    # Real: 185 km
    ('João Pessoa', 'Recife', 120),   # Real: 120 km
    ('Recife', 'Maceió', 256),        # Real: 256 km
    ('Maceió', 'Aracaju', 278),       # Real: 278 km
    ('Aracaju', 'Salvador', 356),     # Real: 356 km
    ('Salvador', 'Feira de Santana', 108), # Real: 108 km
    ('Feira de Santana', 'Vitória da Conquista', 330), # Real: 330 km
    ('Vitória da Conquista', 'Teófilo Otoni', 298), # Real: 298 km
    ('Teófilo Otoni', 'Governador Valadares', 138), # Real: 138 km
    ('Governador Valadares', 'Ipatinga', 103), # Real: 103 km
    ('Ipatinga', 'Belo Horizonte', 216), # Real: 216 km
    ('Belo Horizonte', 'Sete Lagoas', 70), # Real: 70 km
    ('Sete Lagoas', 'Paracatu', 220), # Real: 220 km
    ('Paracatu', 'Unaí', 125),        # Real: 125 km
    ('Unaí', 'Brasília', 162),        # Real: 162 km
    
    # Intermediárias (distâncias reais entre cidades no caminho de Brasília a outras regiões)
    ('Brasília', 'Goiânia', 209),     # Real: 209 km
    ('Goiânia', 'Anápolis', 55),      # Real: 55 km
    ('Anápolis', 'Jataí', 327),       # Real: 327 km
    ('Jataí', 'Rondonópolis', 371),   # Real: 371 km
    ('Rondonópolis', 'Cuiabá', 218),  # Real: 218 km
    ('Cuiabá', 'Campo Grande', 550),  # Real: 550 km
    ('Campo Grande', 'Bonito', 300),  # Real: 300 km
    ('Bonito', 'Jardim', 63),         # Real: 63 km
    ('Jardim', 'Miranda', 72),        # Real: 72 km
    ('Miranda', 'Aquidauana', 61),    # Real: 61 km
    ('Aquidauana', 'Terenos', 150),   # Real: 150 km
    ('Terenos', 'Campo Grande', 40)   # Real: 40 km
]

# Criar um grafo vazio
G = nx.Graph()

# Transferir os dados da lista (graph) para o grafo G
for edge in graph:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Algoritmo de Dijkstra para encontrar o caminho mais curto
def dijkstra_path(graph, start, end):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {}
    unvisited_cities = set(graph)

    while unvisited_cities:
        current_city = min(unvisited_cities, key=lambda city: distances[city])
        unvisited_cities.remove(current_city)

        for neighbor, data in graph[current_city].items():
            distance = distances[current_city] + data['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city

    # Reconstruir o caminho mais curto
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = previous[current]
    path.insert(0, start)

    total_weight = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    return path, total_weight

# Testar o algoritmo com um caminho de 'Natal' para 'Brasília'
start_city = 'Natal'
end_city = 'Brasília'
caminho, peso_total = dijkstra_path(G, start_city, end_city)

# Definir a função de animação
def update_animation(frame):
    plt.clf()  # Limpar a figura atual
    pos = nx.spring_layout(G, seed=220)  # Layout para posicionamento dos nós
    nx.draw_networkx(G, pos)  # Desenhar o grafo completo
    # Destacar os nós e arestas ao longo do caminho
    nx.draw_networkx_nodes(G, pos, nodelist=caminho[:frame + 1], node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=[(caminho[i], caminho[i + 1]) for i in range(frame)], edge_color='r', width=3)

# Configurar e mostrar a animação do grafo
fig, ax = plt.subplots()
pos = nx.spring_layout(G, seed=220)
nx.draw_networkx(G, pos)
ani = FuncAnimation(fig, update_animation, frames=len(caminho), interval=1000, repeat=True)

# Atribuir a animação a uma variável global para garantir persistência
global ani_variable
ani_variable = ani

# Exibir a animação
plt.show()

# Saída para Graphviz (opcional para ferramentas externas de visualização)
print("digraph G {")
for i in range(len(caminho) - 1):
    print(f"{caminho[i]} -> {caminho[i + 1]} [color=red];")
print("}")
print(f"Distância total: {peso_total} km")

# Imprimir o resultado no console
print("Caminho mais curto de", start_city, "para", end_city, ":", caminho)
print("Distância total:", peso_total, "km")

