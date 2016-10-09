from flask import *
import os

import hashlib

testother = Blueprint('testother', __name__, template_folder='views')

@testother.route('/test2', methods=['GET', 'POST'])
def test_route():
	return render_template("index2.html")
