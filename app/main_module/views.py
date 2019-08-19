from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
	return render_template("index.html")