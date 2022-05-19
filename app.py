import os

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template(
        'index.html',
        color='wheat',
        version='v1',
        environment=os.environ.get('ENVIRONMENT', 'development')
    )

@app.route('/database-access')
def database_access():
    environment = os.environ.get('ENVIRONMENT', 'development')
    if environment == 'production':
        return 'FORBIDDEN!!', 403
    else:
        return 'You may pass!', 200

@app.route('/nova-funcionalidade')
def nova_funcionalidade():
    return render_template(
        'pagina.html',
        color=os.environ.get('COLOR', 'gray')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
