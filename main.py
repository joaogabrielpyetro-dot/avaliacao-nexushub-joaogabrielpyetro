startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": 2026,
}

solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

print("--- ETAPA 1: Cadastro da Startup ---")
print(f"Nome da Startup: {startup['nome']}")
print(f"Segmento: {startup['segmento']}")
print(f"Primeiro produto: {solucoes_ativas[0]}")
print()


bancadas = [[1, 0], [0, 1]]

print("--- ETAPA 2: Mapeamento das Bancadas ---")
print("Legenda: 1 = Ocupado | 0 = Livre")
print(f"Setor Norte - Bancada N1 (bancadas[0][0]): {bancadas[0][0]}")
print(f"Setor Norte - Bancada N2 (bancadas[0][1]): {bancadas[0][1]}")
print(f"Setor Sul - Bancada S1 (bancadas[1][0]): {bancadas[1][0]}")
print(f"Setor Sul - Bancada S2 (bancadas[1][1]): {bancadas[1][1]}")

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    dado_1 = arquivo.readline()
    dado_2 = arquivo.readline()
    dado_3 = arquivo.readline()
    dado_4 = arquivo.readline()

print(cabecalho, end="")
print(dado_1, end="")
print(dado_2, end="")
print(dado_3, end="")
print(dado_4, end="")

print("\nAs linhas do CSV foram lidas como textos separados por virgula.")

custo_1 = float(dado_1.split(",")[1])
custo_2 = float(dado_2.split(",")[1])
custo_3 = float(dado_3.split(",")[1])
custo_4 = float(dado_4.split(",")[1])
total = custo_1 + custo_2 + custo_3 + custo_4
print("Valores numericos convertidos para o tipo float.")

print("\n--- PAINEL FINAL ---")
print(f"Nome da startup: {startup['nome']}")
print("Bancada alocada: Bancada N1")
print(f"Valor total de infraestrutura Cloud: R$ {total:.2f}")