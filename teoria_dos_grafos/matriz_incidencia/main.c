#include <stdio.h>
#include "matriz_incidencia.h"

void gerar_dot(int n, int A[n][n]) {
    FILE *file = fopen("grafo.dot", "w");
    if (file == NULL) {
        printf("Erro ao criar arquivo dot.\n");
        return;
    }

    // Início da descrição do grafo
    fprintf(file, "digraph G {\n");

    // Itera sobre a matriz de adjacência para criar as arestas
    for (int linha = 0; linha < n; linha++) {
        for (int coluna = 0; coluna < n; coluna++) {
            if (A[linha][coluna] == 1) {
                fprintf(file, "    %d -> %d;\n", linha, coluna); // Aresta direcionada de 'linha' para 'coluna'
            }
        }
    }

    // Fim da descrição do grafo
    fprintf(file, "}\n");

    fclose(file);
    printf("Arquivo grafo.dot gerado com sucesso.\n");
}

int main() {
    // Definindo o número de nós (tamanho da matriz)
    int n = 4;

    // Matriz de adjacência de exemplo
    int A[4][4] = {
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {1, 0, 0, 1},
        {0, 0, 0, 0}
    };

    // Matriz de incidência, inicialmente vazia (nós x arestas)
    int B[4][16] = {0}; // A matriz pode ter até n*n arcos

    // Exibe a matriz de adjacência
    printf("Matriz de Adjacência:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%2d ", A[i][j]);
        }
        printf("\n");
    }

    // Aguarda o usuário pressionar "Enter"
    printf("\nPressione 'Enter' para exibir a Matriz de Incidência...");
    getchar();

    // Chama a função para converter a matriz de adjacência em matriz de incidência
    converter_matriz_adjacencia_para_incidencia(n, A, B);

    // Exibe a matriz de incidência
    printf("Matriz de Incidência:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n * n; j++) {
            // Só imprime os valores não nulos para manter a formatação
            if (B[i][j] != 0) {
                printf("%2d ", B[i][j]);
            } else {
                printf("   ");
            }
        }
        printf("\n");
    }

    // Gera o arquivo .dot para o Graphviz
    gerar_dot(n, A);

    return 0;
}

