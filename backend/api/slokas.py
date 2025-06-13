from flask import Blueprint, request, jsonify
from services.sloka_guru_service import SlokaGuruService
from models.slokas_database import sloka_db

slokas_bp = Blueprint('slokas', __name__)
sloka_guru = SlokaGuruService()

@slokas_bp.route('/ask', methods=['POST'])
def ask_sloka_guru():
    """Endpoint to ask questions to the Sloka Guru"""
    try:
        data = request.json
        question = data.get('question')
        user_id = data.get('user_id')
        language = data.get('language', 'english')
        
        if not question:
            return jsonify({
                'success': False,
                'message': 'Question is required'
            }), 400
        
        response = sloka_guru.get_response(question, user_id, language)
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/explain', methods=['POST'])
def explain_sloka():
    """Endpoint to get detailed explanation of a specific sloka"""
    try:
        data = request.json
        sloka_text = data.get('sloka')
        user_id = data.get('user_id')
        
        if not sloka_text:
            return jsonify({
                'success': False,
                'message': 'Sloka text is required'
            }), 400
            
        response = sloka_guru.explain_sloka(sloka_text, user_id)
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/daily', methods=['GET'])
def get_daily_sloka():
    """Get the daily sloka with full details"""
    try:
        sloka = sloka_db.get_daily_sloka()
        if not sloka:
            return jsonify({
                'success': False,
                'message': 'No sloka available'
            }), 404
        
        return jsonify({
            'success': True,
            'sloka': sloka,
            'formatted': sloka_db.get_formatted_sloka(sloka['id'])
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/by-id/<sloka_id>', methods=['GET'])
def get_sloka_by_id(sloka_id):
    """Get a specific sloka by ID"""
    try:
        sloka = sloka_db.get_sloka_by_id(sloka_id)
        if not sloka:
            return jsonify({
                'success': False,
                'message': f'Sloka with ID {sloka_id} not found'
            }), 404
        
        return jsonify({
            'success': True,
            'sloka': sloka,
            'formatted': sloka_db.get_formatted_sloka(sloka_id)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/by-category/<category>', methods=['GET'])
def get_slokas_by_category(category):
    """Get all slokas in a specific category"""
    try:
        slokas = sloka_db.get_slokas_by_category(category)
        return jsonify({
            'success': True,
            'category': category,
            'count': len(slokas),
            'slokas': slokas
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/by-guru/<guru_name>', methods=['GET'])
def get_slokas_by_guru(guru_name):
    """Get slokas assigned to a specific guru"""
    try:
        slokas = sloka_db.get_slokas_by_guru(guru_name)
        return jsonify({
            'success': True,
            'guru': guru_name,
            'count': len(slokas),
            'slokas': slokas
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/by-source/<source>', methods=['GET'])
def get_slokas_by_source(source):
    """Get slokas from a specific source text"""
    try:
        slokas = sloka_db.get_slokas_by_source(source)
        return jsonify({
            'success': True,
            'source': source,
            'count': len(slokas),
            'slokas': slokas
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/search', methods=['GET'])
def search_slokas():
    """Search slokas by keyword"""
    try:
        search_term = request.args.get('q', '')
        if not search_term:
            return jsonify({
                'success': False,
                'message': 'Search term is required'
            }), 400
        
        slokas = sloka_db.search_slokas(search_term)
        return jsonify({
            'success': True,
            'search_term': search_term,
            'count': len(slokas),
            'slokas': slokas
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/stats', methods=['GET'])
def get_database_stats():
    """Get statistics about the slokas database"""
    try:
        stats = sloka_db.get_database_stats()
        return jsonify({
            'success': True,
            'database_stats': stats
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/all', methods=['GET'])
def get_all_slokas():
    """Get all slokas with pagination"""
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        all_slokas = sloka_db.slokas_data.get('slokas', [])
        total = len(all_slokas)
        
        # Calculate pagination
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_slokas = all_slokas[start_idx:end_idx]
        
        return jsonify({
            'success': True,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'pages': (total + per_page - 1) // per_page
            },
            'slokas': paginated_slokas
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/categories', methods=['GET'])
def get_categories():
    """Get all available categories"""
    try:
        stats = sloka_db.get_database_stats()
        categories = list(stats['categories'].keys())
        
        return jsonify({
            'success': True,
            'categories': categories,
            'category_counts': stats['categories']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@slokas_bp.route('/sources', methods=['GET'])
def get_sources():
    """Get all available source texts"""
    try:
        stats = sloka_db.get_database_stats()
        
        return jsonify({
            'success': True,
            'sources': stats['available_sources'],
            'source_counts': stats['sources']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
