# Nome do compilador
CC = gcc

# Flags de compilação
CFLAGS = -Wall -Wextra -O2

# Nome do executável
TARGET = matriz_incidencia

# Diretórios
INCLUDE_DIR = include
SRC_DIR = src

# Arquivos fonte
SOURCES = main.c $(SRC_DIR)/matriz_incidencia.c

# Regras de compilação
$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -I$(INCLUDE_DIR) -o $(TARGET) $(SOURCES)

# Limpeza dos arquivos compilados
clean:
	rm -f $(TARGET)

.PHONY: clean

