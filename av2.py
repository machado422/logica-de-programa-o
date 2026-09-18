# ==============================================================================
# PROVA PRATICA AV2 - 3 BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: joao machado
# Data:18/09/2026
# Link do Repositorio:
# ==============================================================================

# Lista inicial de dados brutos
# Formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNCOES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNCAO 1:
    Recebe uma string, remove espacos das pontas e
    converte o texto para letras maiusculas.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNCAO 2:
    Recebe um telefone ou codigo, remove espaços das pontas
    e utiliza fatiamento para extrair os 2 primeiros digitos.
    """
    dado_limpo = dado.strip()
    codigo = dado_limpo[0:2]
    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNCAO 3:
    Percorre a lista de cadastros, separa os dados,
    chama as outras funcoes e exibe os resultados.
    Retorna a quantidade de registros processados.
    """

    total_processado = 0

    # Percorre todos os registros da lista
    for dado in lista_dados:

        # Remove espacos das pontas e separa os dados pelo ";"
        partes = dado.strip().split(";")

        # Separa nome, cargo e telefone
        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        # Chama as funcoes para formatar os dados
        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        # Exibe o cadastro formatado
        print(f"Nome: {nome_formatado}")
        print(f"Cargo/Setor: {cargo_formatado}")
        print(f"DDD/Codigo: {ddd}")
        print("-" * 50)

        # Conta o registro processado
        total_processado += 1

    return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chamada da Funcao 3 passando a lista de dados
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total de registros processados
    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUIDO              ")
    print("==================================================")


# ------------------------------------------------------------------------------
# Execucao do programa
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
