import smtplib
message = """From: From Person <kylejamesbehiels@gmail.com>
To: To Person <kylejamesbehiels@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""
fromaddr = 'kylejamesbehiels@gmail.com'
toaddrs  = 'kylejamesbehiels@gmail.com'
username = 'kylejamesbehiels@gmail.com'
password = 'Bayliner69'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, message)
server.quit()


s
