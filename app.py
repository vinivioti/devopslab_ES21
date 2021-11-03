from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Vou dominar essa ferramenta, acredite !!"

if __name__ == '__main__':
    app.run(debug=True)
