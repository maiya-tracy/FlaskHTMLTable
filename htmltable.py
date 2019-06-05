from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
	return render_template('index.html', phrase="hello", times=5)

@app.route('/table')
def html_table():
	users = [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'John', 'last_name' : 'Supsupin'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	]
	return render_template("htmltable.html", users=users)




@app.errorhandler(404)
def page_not_found(error):
	return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.
