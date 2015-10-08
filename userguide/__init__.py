from flask import Flask
app = Flask(__name__)

const = {
    'layout': 'hello-world',
    'dash.react': 'making-dash-apps-interactive'
}

import userguide.index
import userguide.helloworld
import userguide.dash_react
