# ==============================================================================
# PROVA PRATICA AV1 - 3 BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: joao vitor machado
# Data:
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# Percorre a lista usando for e range()
for i in range(len(cadastros_brutos)):

   # 1. Remove os espaços extras do inicio e fim do cadastro atual
   cadastro = cadastros_brutos[i].strip()

   # 2. Separa o nome e o telefone
   nome, telefone = cadastro.split(";")

   # 3. Converte o nome para letras MAIUSCULAS
   nome = nome.upper()

   # 4. Extrai o DDD (2 primeiros digitos do telefone)
   ddd = telefone[0:2]

   # 5. Exibe o resultado padronizado no terminal
   print(f"Funcionario: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("             PROCESSAMENTO CONCLUIDO              ")
print("==================================================")
