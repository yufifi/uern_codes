import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados para o gráfico de cidades brasileiras (com 50 cidades no total e 25 intermediárias)
graph = [
    ('Natal', 'João Pessoa', 185), ('João Pessoa', 'Recife', 120), ('Recife', 'Maceió', 258),
    ('Maceió', 'Aracaju', 275), ('Aracaju', 'Salvador', 350), ('Salvador', 'Feira de Santana', 108),
    ('Feira de Santana', 'Vitória da Conquista', 291), ('Vitória da Conquista', 'Teófilo Otoni', 270),
    ('Teófilo Otoni', 'Governador Valadares', 138), ('Governador Valadares', 'Ipatinga', 100),
    ('Ipatinga', 'Belo Horizonte', 215), ('Belo Horizonte', 'Sete Lagoas', 75),
    ('Sete Lagoas', 'Paracatu', 225), ('Paracatu', 'Unaí', 115), ('Unaí', 'Brasília', 140),
    ('Brasília', 'Goiânia', 209), ('Goiânia', 'Anápolis', 55), ('Anápolis', 'Jataí', 327),
    ('Jataí', 'Rondonópolis', 234), ('Rondonópolis', 'Cuiabá', 219), ('Cuiabá', 'Campo Grande', 694),
    ('Campo Grande', 'Bonito', 300), ('Bonito', 'Jardim', 63), ('Jardim', 'Miranda', 60),
    ('Miranda', 'Aquidauana', 30), ('Aquidauana', 'Terenos', 120), ('Terenos', 'Campo Grande', 32),
    ('Natal', 'Fortaleza', 537), ('Fortaleza', 'Teresina', 634), ('Teresina', 'São Luís', 446),
    ('São Luís', 'Belém', 806), ('Belém', 'Macapá', 328), ('Belém', 'Boa Vista', 1936),
    ('Boa Vista', 'Manaus', 748), ('Manaus', 'Porto Velho', 889), ('Porto Velho', 'Rio Branco', 500),
    ('Rio Branco', 'Cruzeiro do Sul', 648), ('Cruzeiro do Sul', 'Tarauacá', 397),
    ('Brasília', 'Caldas Novas', 286), ('Caldas Novas', 'Trindade', 131),
    ('Trindade', 'Uberlândia', 257), ('Uberlândia', 'Ituiutaba', 126),
    ('Ituiutaba', 'Patrocínio', 181), ('Patrocínio', 'Uberaba', 235),
    ('Uberaba', 'Ribeirão Preto', 113), ('Ribeirão Preto', 'Franca', 93),
    ('Franca', 'Barretos', 106), ('Barretos', 'São José do Rio Preto', 122)
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

# Atribuir a animação a uma variável para que não seja deletada antes de exibir
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

