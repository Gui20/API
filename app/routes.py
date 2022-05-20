from API import app
import os


@app.route('/api/v1/<string:x>', methods=['GET', 'POST'])
def getUSD(x):
    os.mkdir(x)
    return x
