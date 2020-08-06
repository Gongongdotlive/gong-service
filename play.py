import flask
from flask import request, jsonify
import xml.etree.ElementTree as ET

app = flask.Flask(__name__)
app.config["DEBUG"] = True

tree = ET.parse('doc.xml')
root = tree.getroot()

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []
    for ticket in root.iter('ticket'):
        new_ticket = int(ticket.text) + 1
        ticket.text = str(new_ticket)
        ticket.set('used', 'yes')

    tree.write('doc.xml')

    return jsonify(results)

app.run()