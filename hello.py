from flask import Flask, render_template

# create flask instance
app = Flask(__name__)



# route
@app.route('/')
def index():
	first_name = "John"
	return render_template("index.html", first_name=first_name)


@app.route('/user/<name>')
def user(name):
	return render_template("user.html", user_name=name)

@app.errorhandler(404):
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500):
def internal_server_error(e):
	return render_template("500.html"), 500

