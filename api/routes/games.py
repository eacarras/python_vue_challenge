from flask import Blueprint

games_bp = Blueprint('games', __name__)

@games_bp.route('/health')
def health():
  return 'The server is up and running'
