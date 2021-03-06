#!/usr/bin/python

'''
The purpose of thie script is to verify the user's information when they
try to login in using the user login webpage.
The script creates, handles, and removes cookies.
If the user's information is valid, it will welcome the user and proceed to the
shopingcart webpage.
If the user previously had items in the cart, did not complete their purchase, and
another user has not logged in yet, the script will welcome them back.
If the user if the user did complete their purchase or another user did log in, the
script will just welcome the user.
If the user's information is invalid, it will tell them their username/password
is incorrect.
'''


import cgi
import os
import sys
import mysql.connector

sys.path.append('/home/coursework/public_html/Builder/')

from Database import *

con = mysql.connector.connect(user=user, password=passwd, host=host, database=db)
cursor = con.cursor(buffered=True)

form_items = cgi.FieldStorage()
useriden = form_items.getvalue('userident')
user_pass = form_items.getvalue('user_passwd')


command = "SELECT * FROM `UserAccounts` where id=%s and password=%s"
cursor.execute(command, (useriden, user_pass))
result = cursor.fetchall()
if cursor.rowcount == 1:
	print """Content-type:text/html\r\n\r\n
	  	<html>
		<head>
		<script type="text/javascript">
		function createCookie(cname,cvalue,expiretime){
		var d = new Date();
		d.setTime(d.getTime() + (expiretime*24*60*60*1000));
		var expires = "expires=" + d.toGMTString();
		document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
		}
		function getCookie(cname) {
		var name = cname + "=";
		var decodedCookie = decodeURIComponent(document.cookie);
		var ca = decodedCookie.split(';');
		for(var i = 0; i < ca.length; i++){
		var c = ca[i];
		while (c.charAt(0) == ' '){
			c = c.substring(1);
		}
		if(c.indexOf(name) == 0){
			return c.substring(name.length, c.length);
		} } return " "; }
		function removeCookies(){
			createCookie("username","",-1);
			createCookie("cart_items","",-1);
		}
		function checkCookie() {
		var user=getCookie("username")
		if(user == '%s'){
			alert('Welcome back ' + user + '!');
			window.location.href = 'http://localhost/~coursework/cgi-bin/shoppingcart.cgi'
		}else if(user != ""){
			removeCookies();	
			createCookie("username",'%s',1);
			alert('Welcome %s!');
			window.location.href = 'http://localhost/~coursework/cgi-bin/shoppingcart.cgi'

		}
		else{
			alert('Welcome %s!');
			createCookie("username",'%s',1);
			window.location.href = 'http://localhost/~coursework/cgi-bin/shoppingcart.cgi'
		}}
		</script>
		</head>
		<body>
		<script type="text/javascript">
			checkCookie();	
		</script>		
		</body>
		</html>"""%(useriden,useriden,useriden,useriden,useriden)
else:
	print """Content-type:text/html\r\n\r\n
		<html>
		<body>
		<script type='text/javascript'>
		alert('Username/Password is Incorrect!')
		window.location.href='http://localhost/~coursework/cgi-bin/userlogin.cgi'
		</script>
		</body>
		</html>"""

cursor.close()
con.close()
