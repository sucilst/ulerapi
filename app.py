from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Halo Assertible"

@app.route("/hagemaru")
def hagemaru():
	return "Halo"

if __name__ == "__main__":
	app.run()
