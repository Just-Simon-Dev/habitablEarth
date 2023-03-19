from flask import Flask, jsonify, request
from cities.city import City
from countries.Country import Country
from datetime import datetime
from flask_cors import CORS
import warnings

app = Flask(__name__)
CORS(app, resources={r'/api/*': { "origins": "*" }})

warnings.filterwarnings("ignore")

@app.route('/api/countries', methods=["GET"])
def get_countries():
	end_date = datetime.strptime(request.args['end_date'], '%Y-%m-%d')
	country_name = request.args['country']

	country = Country()
	steps = country.calculate_step(end_date)
	
	temperatures = country.predict_temperature_for_country(steps, country_name)
	return jsonify(temperatures)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('certificate.crt', 'private.key'))

# @app.route('/api/cities', methods=["GET"])
# def get_cities():
# 	name = request.args['city']
# 	_from = datetime.strptime(request.args['from'], '%Y-%m-%d')
# 	_to = datetime.strptime(request.args['to'], '%Y-%m-%d')

# 	city = City(name)
# 	temperatures = city.get_temperature(_from, _to)
# 	return jsonify(temperatures)
