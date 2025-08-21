from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        operacao = request.form["operacao"]

        if operacao == "soma":
            resultado = n1 + n2
        elif operacao == "subtracao":
            resultado = n1 - n2
        elif operacao == "multiplicacao":
            resultado = n1 * n2
        elif operacao == "divisao":
            resultado = n1 / n2 if n2 != 0 else "Erro: divisão por zero"
    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)