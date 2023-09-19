from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Gibt den Text 'Willkommen bei meiner Flask-App!' zurück."""
    return 'Willkommen bei meiner Flask-App!'

@app.route('/info', methods=['GET'])
def info():
    """Gibt den Text 'Dies ist die Info-Seite.' zurück."""
    return 'Dies ist die Info-Seite.'

@app.route('/user/<username>', methods=['GET'])
def user(username):
    """Gibt den Text 'Hallo, [username]!' zurück, wobei [username] durch den in der URL angegebenen Benutzernamen ersetzt wird."""
    return f'Hallo, {username}!'

@app.route('/post', methods=['POST'])
def post_data():
    """Akzeptiert Daten und gibt den Text 'Daten erfolgreich erhalten!' zurück."""
    return 'Daten erfolgreich erhalten!'

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """Bei einem GET-Request gibt es den Text 'Bitte geben Sie Ihr Feedback ab.' zurück. Bei einem POST-Request gibt es den Text 'Danke für Ihr Feedback!' zurück."""
    if request.method == 'GET':
        return 'Bitte geben Sie Ihr Feedback ab.'
    elif request.method == 'POST':
        return 'Danke für Ihr Feedback!'

@app.route('/item/<int:item_id>', methods=['GET'])
def item(item_id):
    """Gibt den Text 'Artikel-ID: [item_id]' zurück, wobei [item_id] durch die in der URL angegebene Artikel-ID ersetzt wird."""
    return f'Artikel-ID: {item_id}'

if __name__ == '__main__':
    app.run()