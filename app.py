from flask import *
app=Flask(__name__,
        static_folder="static",
        static_url_path="/"
)

@app.route("/") #Decorator of the function based on function provide additional function
def home():
	return render_template("index.html")

@app.route("/learn1109") #Decorator of the function based on function provide additional function
def learn():
	return render_template("learn1109.html")

@app.route("/LnCcs1109") #Decorator of the function based on function provide additional function
def learnccs():
	return render_template("LnCcs1109.html")
@app.route("/test")
def test():
	return "This is Test"


if __name__ =="__main__":

        app.run(host=localhost,port=8071,debug=True,ssl_context=('/etc/letsencrypt/live/bingbing.hopto.org/cert.pem','/etc/letsencrypt/live/bingbing.hopto.org/privkey.pem'))

