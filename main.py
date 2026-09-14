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