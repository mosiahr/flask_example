from app import app

from toasters.blueprint import toasters

import view

app.register_blueprint(toasters, url_prefix='/toasters')  #регистрируем blueprint


if __name__ == '__main__':
    app.run()