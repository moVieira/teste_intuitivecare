from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Caminho do arquivo CSV
csv_path = 'C:\\Users\\PC1\\Desktop\\meu_projeto\\dados_csv\\dados_cadastrais\\Relatorio_cadop.csv'
# Testar a leitura das colunas do CSV
try:
    df = pd.read_csv(csv_path, encoding='utf-8', sep=',', on_bad_lines='skip')
    print("CSV carregado com sucesso!")
    print("Colunas encontradas no CSV:", df.columns.tolist())  # Lista os nomes das colunas
except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")

# Testar a leitura das primeiras linhas para verificar o formato
try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        print("Primeiras 10 linhas do CSV:")
        for i in range(10):
            print(f.readline().strip())  # Remove espaços extras
except Exception as e:
    print(f"Erro ao abrir o arquivo: {e}")

# Carregar os dados do CSV com tratamento de erro
try:
    df = pd.read_csv(csv_path, encoding='utf-8', sep=';', on_bad_lines='skip')
    print("CSV carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")

@app.route('/buscar_operadora', methods=['GET'])
def buscar_operadora():
    termo = request.args.get('termo', '').lower()
    if not termo:
        return jsonify({"erro": "Informe um termo de busca"}), 400

    # Ajuste para a coluna correta
    coluna_nome = 'Nome_Fantasia'  # Verifique se esse é o nome correto da coluna no seu CSV
    if coluna_nome not in df.columns:
        return jsonify({"erro": f"Coluna '{coluna_nome}' não encontrada no CSV"}), 500

    # Filtrar operadoras que contêm o termo na coluna de nome
    resultados = df[df[coluna_nome].astype(str).str.lower().str.contains(termo, na=False)]

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
