from app import app
from flask import (json, Response)

numbers_to_add = list(range(10000001))

@app.route('/total')
def api_default_total():
    data = {
        'total'  : sum(numbers_to_add)
    }
    js = json.dumps(data)
    return Response(js, status=200, mimetype='application/json')
