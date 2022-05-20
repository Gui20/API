from flask import Flask
import os
app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/api/v1/<string:x>', methods=['GET', 'POST'])
def getUSD(x):
    os.mkdir(x)
    return x

app.run(host="0.0.0.0")
