#!/usr/bin/python

'''
The purpose of this script is the allow the user to register an account.
The user must enter a first name, last name, user id, password, and email.
The first name can only be alpha characters and must be between 2-25 characters long.
The last name can only be alpha characters and must be between 2-50 characters long.
The user id can only be alphanumeric characters and must be between 2-20 characters long.
The password must be betweeen 8-16 characters long
The email address must be in valid email format (ie. @gmail.com) and must be between 8-50 characters long.
This script also does a password match to ensure the user correctly entered their password. 
'''

import cgi
from account_creation import *


print"""Content-type:text/html\r\n\r\n
<html>
<head>
<title>Shopper Registration Screen</title>
</head>
<body>
<h1>Registration</h1><br>
<form name='reg' action='http://localhost/~coursework/cgi-bin/account_creation.py' method='get'>
First Name: <input type='text' name='first_name' value="%s" style="margin-left:60px; " pattern="[A-Za-z]{2,25}" title="Only alpha characters allowed and First name must be  between 2-25 characters long" required><br>
Last Name: <input type='text' name='last_name' value="%s" style="margin-left:63px; " pattern="[A-Za-z]{2,50}" title="Only alpha characters allowed and Last name must be between 2-50 characters long" required><br>  
User ID: <input type='text' name='user_id' value="%s" style="margin-left:90px;" pattern="[A-za-z0-9]{2,20}" title="Only alphanumeric characters allowed and User ID must be between 2-20 characters long" required><br>
Password: <input type='password' name='passwd' style="margin-left:72px;" pattern=".{8,16}" title="Password must be between 8-16 characters long" required><br>
Confirm Password: <input type='password' name=conf_passwd required><br>
Email: <input type='email' name='email' value="%s" style="margin-left:106px;" pattern=".{8,50}" title="Email must be between 8-50 characters long"required><br>
<input type = 'submit' onclick='return validateInformation();' value='Register'/>
<script type='text/javascript'>
function validateInformation(){
if(reg.passwd.value != reg.conf_passwd.value){
reg.conf_passwd.setCustomValidity('Passwords Do not Match!');} else {
reg.conf_passwd.setCustomValidity(''); return true;}}</script>
</form>
</body>
</html>
"""%(f_name,l_name,userid,email_add)

