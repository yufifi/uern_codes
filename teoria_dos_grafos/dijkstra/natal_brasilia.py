import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grafo de cidades brasileiras com pelo menos 23 cidades intermediárias entre Natal e Brasília
graph = [
    ('Natal', 'João Pessoa', 185), ('João Pessoa', 'Recife', 120), 
    ('Recife', 'Maceió', 258), ('Maceió', 'Aracaju', 275), 
    ('Aracaju', 'Salvador', 350), ('Salvador', 'Feira de Santana', 108), 
    ('Feira de Santana', 'Vitória da Conquista', 302), ('Vitória da Conquista', 'Teófilo Otoni', 289),
    ('Teófilo Otoni', 'Governador Valadares', 164), ('Governador Valadares', 'Ipatinga', 100),
    ('Ipatinga', 'Belo Horizonte', 217), ('Belo Horizonte', 'Sete Lagoas', 72),
    ('Sete Lagoas', 'Curvelo', 104), ('Curvelo', 'Montes Claros', 301), 
    ('Montes Claros', 'Pirapora', 142), ('Pirapora', 'Paracatu', 148),
    ('Paracatu', 'Unaí', 160), ('Unaí', 'Brasília', 160),
    ('Brasília', 'Goiânia', 209), ('Goiânia', 'Anápolis', 54), 
    ('Anápolis', 'Caldas Novas', 165), ('Caldas Novas', 'Catalão', 120), 
    ('Catalão', 'Uberlândia', 113), ('Uberlândia', 'Uberaba', 105), 
    ('Uberaba', 'Franca', 105), ('Franca', 'Ribeirão Preto', 88), 
    ('Ribeirão Preto', 'São Carlos', 100), ('São Carlos', 'Araraquara', 45),
    ('Araraquara', 'São José do Rio Preto', 170), ('São José do Rio Preto', 'Barretos', 85),
    ('Barretos', 'Franca', 82), ('Franca', 'Batatais', 68),
    ('Batatais', 'Ribeirão Preto', 45), ('Ribeirão Preto', 'Bebedouro', 100),
    ('Bebedouro', 'Barretos', 42), ('Barretos', 'São José do Rio Preto', 78),
    # Cidades intermediárias adicionais
    ('Goiânia', 'Itumbiara', 207), ('Itumbiara', 'Uberlândia', 114), # Nova rota passando por Itumbiara
    ('Anápolis', 'Jaraguá', 125), ('Jaraguá', 'Uruaçu', 132), # Mais cidades em Goiás
    ('Brasília', 'Formosa', 81) # Adicionada cidade próxima de Brasília
]

# Criação do grafo
G = nx.Graph()

# Adiciona os dados do grafo
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

# Teste do algoritmo com o caminho de 'Natal' para 'Brasília'
start_city = 'Natal'
end_city = 'Brasília'
caminho, peso_total = dijkstra_path(G, start_city, end_city)

# Função para animação
def update_animation(frame):
    plt.clf()  # Limpa a figura atual
    pos = nx.spring_layout(G, seed=220)  # Layout para posicionamento dos nós
    nx.draw_networkx(G, pos)  # Desenha o grafo completo
    # Destaque os nós e arestas ao longo do caminho
    nx.draw_networkx_nodes(G, pos, nodelist=caminho[:frame + 1], node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=[(caminho[i], caminho[i + 1]) for i in range(frame)], edge_color='r', width=3)

# Configura a animação do grafo
fig, ax = plt.subplots()
pos = nx.spring_layout(G, seed=220)
nx.draw_networkx(G, pos)
ani = FuncAnimation(fig, update_animation, frames=len(caminho), interval=1000, repeat=True)
plt.show()

# Saída para visualização em Graphviz (opcional)
print("digraph G {")
for i in range(len(caminho) - 1):
    print(f"{caminho[i]} -> {caminho[i + 1]} [color=red];")
print("}")
print(f"Distância total: {peso_total} km")

# Exibe o resultado no console
print("Caminho mais curto de", start_city, "para", end_city, ":", caminho)
print("Distância total:", peso_total, "km")

