from flask import Flask, request, Response
import os
import datetime
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_information():
    try:
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')

        if not slack_name or not track:
            response_data = {'error': 'Both slack_name and track are required params', 'status_code': 400}
            return Response(json.dumps(response_data, indent=4), content_type='application/json'), 400

        current_day = datetime.datetime.now().strftime('%A')
        # Get the true current UTC time
        true_current_utc_time = datetime.datetime.utcnow()

        # Format the current UTC time in ISO 8601 format
        utc_time = true_current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        github_file_url = 'https://github.com/DavidIfebueme/HNG-Backend-Tasks/blob/master/app.py'
        github_repo_url = 'https://github.com/DavidIfebueme/HNG-Backend-Tasks'
        status_code = 200  # for success

        # Create an ordered dictionary with the desired order of keys
        response_info = OrderedDict([
            ('slack_name', slack_name),
            ('current_day', current_day),
            ('utc_time', utc_time),
            ('track', track),
            ('github_file_url', github_file_url),
            ('github_repo_url', github_repo_url),
            ('status_code', status_code)
        ])

        return Response(json.dumps(response_info, indent=4), content_type='application/json') # for some weird reason I just wanted it vertical :-)

    except Exception as e:
        response_data = {'error': str(e), 'status_code': 500}
        return Response(json.dumps(response_data, indent=4), content_type='application/json'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
