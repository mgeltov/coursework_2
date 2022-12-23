from flask import Flask, render_template

from bp_main.views import bp_main
from bp_api.api import bp_api

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(bp_api)
app.register_blueprint(bp_main)

@app.errorhandler(404)
def error_404(e):
    text = "Нет такой страницы"
    return render_template('error.html', text=text)

@app.errorhandler(500)
def error_500(e):
    text = "Сломался временно сервер"
    return render_template('error.html', text=text)


if __name__ == '__main__':
    app.run()