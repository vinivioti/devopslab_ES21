from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Sapohha é muito legal !!!"

if __name__ == '__main__':
    app.run(debug=True)
