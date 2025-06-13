from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile', methods=['GET'])
def get_user_profile():
    return jsonify({
        'success': True,
        'message': 'User profile endpoint'
    })

@users_bp.route('/preferences', methods=['POST'])
def save_user_preferences():
    return jsonify({
        'success': True,
        'message': 'Preferences saved'
    })
