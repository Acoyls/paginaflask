from flask import Flask, jsonify,render_template,request
import os

app = Flask(__name__)


@app.route('/',  methods = ('GET','POST'))
def index():
    edad = request.form['edad']
    if edad < 18:
        return render_template('menoredad.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
