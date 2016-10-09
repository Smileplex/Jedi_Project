from flask import *
import os

main = Blueprint('main', __name__, template_folder='views')


@main.route('/test/')
def main_route():	
    return render_template("index.html")



