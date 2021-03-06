#!/usr/bin/python

'''
The purpose of this script is to let the user know that an email
of their receipt has been sent to them. It also calls a function
from the email receipt module which sends the email.
'''

import email_receipt
import cgi

form_items = cgi.FieldStorage()
items = form_items.getvalue('purchased_items')
sale_total = form_items.getvalue('total')
f_name = form_items.getvalue('f_name')
l_name = form_items.getvalue('l_name')
	
print """Content-type:text/html\r\n\r\n
	<html>
	<body>
	<p><b> Receipt has been sent.</b></p>
	<p><b> You should be receiving it shortly.</b></p>
	</body>
	</html>"""

email_receipt.sendEmail(items,sale_total,f_name,l_name)
