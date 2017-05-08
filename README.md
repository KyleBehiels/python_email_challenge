# python_email_challenge
A coding challenge presented by Lee Bergstrand. Simple HTML5 form, styled with bootstrap 3.0 that uses a python script to send form details via email.

----------------QUICKSTART GUIDE----------------
1. Open variables.txt

2. Fill in the information based on your email address and provider

	-SMTP_SERVER the host of your email address (gmail --> smtp.gmail.com)
	
	-SMTP_PORT the port that your email address is hosted on (gmail --> 587)
	
	-EMAIL & PASSWORD are the email and password that you use to login
	
3. Save variables.txt
4. Edit simple_form.html to suit your needs. This implementation handles infinite fields until you excede the size limit of an email.

   Just make sure that you submit the form with the POST method
   
5. Host the web application.

	-Submitted credentials will be mailed as a formatted string in the following format:
	
		field_name : field_value field2_name : field2_value
		
----------------/QUICKSTART GUIDE----------------

----------------VARIABLES.TXT FOR POPULAR PROVIDERS----------------

If your email provider is not listed a quick google search:

______ smtp configuration 

Should get you the information that you need. (_______ is your email provider)

____________________________________________________________________
Gmail
____________________________________________________________________
EMAIL:youremail@gmail.com

PASSWORD:yourpassword

SMTP_SERVER:smtp.gmail.com

SMTP_PORT:587
_____________________________________________________________________
Live/Hotmail
_____________________________________________________________________
EMAIL:youremail@live.com

PASSWORD:yourpassword

SMTP_SERVER:smtp.live.com

SMTP_PORT:465
_____________________________________________________________________
Yahoo
_____________________________________________________________________
EMAIL:youremail@yahoo.com

PASSWORD:yourpassword

SMTP_SERVER:smtp.mail.yahoo.com

SMTP_PORT:465(sometimes 587)
_____________________________________________________________________

----------------/VARIABLES.TXT FOR POPULAR PROVIDERS----------------


----------------DISCLAIMER----------------

This system is no more than a template that can be used to set up a system of retrieving credentials. Nothing is encrypted by default. Use at your own risk.

----------------/DISCLAIMER----------------









