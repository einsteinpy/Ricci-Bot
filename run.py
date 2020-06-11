from baldrick import create_app

import baldrick.plugins.circleci_artifacts
import baldrick.plugins.github_milestones
import baldrick.plugins.github_pull_requests
import baldrick.plugins.github_pushes
import baldrick.plugins.github_towncrier_changelog

app = create_app('Ricci-Bot')

import os
port = int(os.environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port, debug=False)
