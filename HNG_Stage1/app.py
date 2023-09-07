from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])

def get_infomation():
    try:
        slack_name = request.args.get('slack_name')
        track = request.args.get('track')

        if not slack_name or not track:
            return jsonify({'error': 'Both slack_name and track are required params', 'status_code': 400}), 400

        day_of_week = datetime.datetime.now().strftime('%A')
        current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        github_mainfile_url = request.args.get('github_mainfile_url')
        github_repo_url = request.args.get('github_repo_url')
        status_code = 200 # for success

        response_info = {
            'slack_name': slack_name,
            'day_of_week': day_of_week,
            'current_utc_time': current_utc_time,
            'github_mainfile_url': github_mainfile_url,
            'github_repo_url': github_repo_url,
            'status_code': status_code
        }

        return jsonify(response_info)

    except Exception as e:
        return jsonify({'error': str(e), 'status_code': 500}), 500    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)