from flask import Blueprint, jsonify
from secrets import token_hex


session_bp = Blueprint('session', __name__)
TOKEN_LENGTH = 16

@session_bp.route('/health')
def health():
  return 'The server is up and running'

@session_bp.route('/new_session')
def new_session():
  session_token = token_hex(TOKEN_LENGTH)
  # TODO: SEND TOKEN TO DATABASE
  return jsonify({
    'message': 'New session created successfully',
    'token': session_token,
  }), 201