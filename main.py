from flask import Flask, request

app = Flask(__name__)


# TODO: Implementiere eine Route für '/', die bei einem GET-Request den Text 'Willkommen bei meiner Flask-App!' zurückgibt.
def home():
    """Gibt den Text 'Willkommen bei meiner Flask-App!' zurück."""
    pass


# TODO: Implementiere eine Route für '/info', die bei einem GET-Request den Text 'Dies ist die Info-Seite.' zurückgibt.
def info():
    """Gibt den Text 'Dies ist die Info-Seite.' zurück."""
    pass


# TODO: Implementiere eine Route für '/user/<username>', die bei einem GET-Request den Text 'Hallo, [username]!' zurückgibt, wobei [username] durch den in der URL angegebenen Benutzernamen ersetzt wird.
def user(username):
    """Gibt den Text 'Hallo, [username]!' zurück, wobei [username] durch den in der URL angegebenen Benutzernamen ersetzt wird."""
    pass


# TODO: Implementiere eine Route für '/post', die bei einem POST-Request den Text 'Daten erfolgreich erhalten!' zurückgibt.
def post_data():
    """Akzeptiert Daten und gibt den Text 'Daten erfolgreich erhalten!' zurück."""
    pass


# TODO: Implementiere eine Route für '/feedback', die bei einem GET-Request den Text 'Bitte geben Sie Ihr Feedback ab.' zurückgibt und bei einem POST-Request den Text 'Danke für Ihr Feedback!' zurückgibt.
def feedback():
    """Bei einem GET-Request gibt es den Text 'Bitte geben Sie Ihr Feedback ab.' zurück. Bei einem POST-Request gibt es den Text 'Danke für Ihr Feedback!' zurück."""
    pass


# TODO: Implementiere eine Route für '/item/<int:item_id>', die bei einem GET-Request den Text 'Artikel-ID: [item_id]' zurückgibt, wobei [item_id] durch die in der URL angegebene Artikel-ID ersetzt wird.
def item(item_id):
    """Gibt den Text 'Artikel-ID: [item_id]' zurück, wobei [item_id] durch die in der URL angegebene Artikel-ID ersetzt wird."""
    pass


if __name__ == '__main__':
    app.run(debug=True)