from flask import render_template

from application import app
from application.models import 5eGenerator
from application.forms import 5eGeneratorForm

from Service2/namegen import app
from Service3/statsgen import app

# 5e chargen stuff

@app.route('/dndchargen/1', methods=['GET', 'POST'])
def generate():
	form = request.data.decode('UTF-8')
	charname=requests.post(
