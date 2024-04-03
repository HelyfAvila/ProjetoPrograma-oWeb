from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para calcular o tipo de triângulo a partir dos parâmetros passados na URL
@app.route('/calc-triangulo')
def tipotriangulo():
    # Obtém os parâmetros da URL
    args = request.args
    lado1_str = args.get('lado1')
    lado2_str = args.get('lado2')
    lado3_str = args.get('lado3')

    # Verifica se os parâmetros foram fornecidos
    if lado1_str is None or lado2_str is None or lado3_str is None:
        return 'Erro: Todos os lados do triângulo devem ser fornecidos na URL.'

    # Converte os parâmetros para números de ponto flutuante
    try:
        lado1 = float(lado1_str)
        lado2 = float(lado2_str)
        lado3 = float(lado3_str)
    except ValueError:
        return 'Erro: Os lados do triângulo devem ser números válidos.'

    # Verifica se os lados são maiores que zero
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return 'Erro: Os lados do triângulo devem ser maiores que zero.'

    # Verifica se os lados formam um triângulo válido
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return 'Erro: As medidas fornecidas não formam um triângulo válido.'

    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        tipo = 'Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'

    # Retorna o resultado em uma página HTML
    return render_template('calc.html', tipo=tipo)

# Rota para calcular o tipo de triângulo a partir dos dados de um formulário POST
@app.route('/calc-triangulo-post', methods=['GET','POST'])
def tipoTriangulopost():
    if request.method == 'POST':
        # Obtém os dados do formulário
        lado1 = float(request.form.get('lado1', 0))
        lado2 = float(request.form.get('lado2', 0))
        lado3 = float(request.form.get('lado3', 0))
        
        # Verifica se os lados são maiores que zero
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            return 'Erro: Os lados do triângulo devem ser maiores que zero.'

        # Verifica se os lados formam um triângulo válido
        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            return 'Erro: As medidas fornecidas não formam um triângulo válido.'

        # Verifica o tipo de triângulo
        if lado1 == lado2 == lado3:
            tipo = 'Equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            tipo = 'Isósceles'
        else:
            tipo = 'Escaleno'
        
        return render_template('calcpost.html', tipo=tipo)

    # Retorna o resultado em uma página HTML
    return render_template('calcpost.html', tipo=None)

# Rota para calcular a média de notas
@app.route('/media-notas', methods=['GET', 'POST'])
def media():
    if request.method == 'POST':
        # Obtém as notas do formulário
        nota1 = float(request.form.get('nota1', 0))
        nota2 = float(request.form.get('nota2', 0))
        nota3 = float(request.form.get('nota3', 0))
        nota4 = float(request.form.get('nota4', 0))

        # Calcula a média
        media = (nota1 + nota2 + nota3 + nota4) / 4
        # Determina a classificação
        if media < 6:
            classificacao = 'REPROVADO'
        else:
            classificacao = 'APROVADO'

        # Retorna o resultado em uma página HTML
        return render_template('media.html', media=media, classificacao=classificacao)
    
    # Se o método não for POST, retorna None para média e classificação
    return render_template('media.html', media=None, classificacao=None)

# Executa o aplicativo Flask
if __name__ == "__main__":
    # Ativa o modo de depuração
    app.run(debug=True)
