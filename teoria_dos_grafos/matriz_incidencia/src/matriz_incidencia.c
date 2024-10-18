#include <stdio.h>
#include "matriz_incidencia.h"

// Função que converte a matriz de adjacência A em uma matriz de incidência B
void converter_matriz_adjacencia_para_incidencia(int n, int A[n][n], int B[n][n * n]) {
    int linha, coluna, arco = 0;

    // Itera sobre todas as linhas (nós)
    for (linha = 0; linha < n; linha++) {
        // Itera sobre todas as colunas (nós)
        for (coluna = 0; coluna < n; coluna++) {
            // Verifica se há uma aresta entre o nó 'linha' e o nó 'coluna'
            if (A[linha][coluna] == 1) {
                arco++; // Incrementa o número de arcos (arestas)
                
                // Inicializa a coluna da matriz de incidência
                for (int k = 0; k < n; k++) {
                    B[k][arco - 1] = 0;
                }

                // Define os valores para o arco: origem (1) e destino (-1)
                B[linha][arco - 1] = 1;     // O nó de origem tem valor 1
                B[coluna][arco - 1] = -1;    // O nó de destino tem valor -1
            }
        }
    }
}

