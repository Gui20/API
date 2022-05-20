from flask import Flask
from sqlalchemy import create_engine
import os

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/v1/<string:nome>&<string:idade>', methods=['GET', 'POST'])
def getUSD(nome, idade):
    engine = create_engine('postgresql://postgres:123456@serverioutility.hopto.org/teste')
    engine.execute(f"INSERT INTO cachorro (nome,idade) VALUES ('{nome}','{idade}')")
    return "deu bom"


port = int(os.environ.get('PORT', 5050))
app.run(host="0.0.0.0", port=port)

