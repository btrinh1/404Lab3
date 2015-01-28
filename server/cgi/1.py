#!/usr/bin/env python
import cgi
 
form = cgi.FieldStorage()
name = form.getvalue('name')
family = form.getvalue('family')
bday = form.getvalue('birthdate')
hobby = form.getvalue('main hobby')

print """Content-Type: text/html

<!DOCTYPE html>
<html>
<form method="get" action="2.py">
name: <input type="text" name="name" /> 
<div> family: <input type="text" name="family" /> </div>
<div> <input type="submit" value="Send"> </div>
</form>

<h1> <u> Results: </u> </h1>
 name: %s <br/>
 family: %s <br/>
 birthdate: %s <br/>
 main hobby: %s <br/>
</html>""" % (name, family, bday, hobby)