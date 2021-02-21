from flask import Flask

from routes.games import games_bp
from routes.session import session_bp 


app = Flask('api_game')

# Declaration of routes
app.register_blueprint(games_bp, url_prefix='/games')
app.register_blueprint(session_bp, url_prefix='/session')

app.run()
