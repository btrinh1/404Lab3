#!/usr/bin/env python
import cgi
 
form = cgi.FieldStorage()
name = form.getvalue('name')
family = form.getvalue('family')

print """Content-Type: text/html
 
<!DOCTYPE html>
<html>

<form method="get" action="1.py">
name: <input type="text" name="name" />
<div> family: <input type="text" name="family" /> </div>
<div> birthdate: <input type="text" name="birthdate" /> </div>
<diuv> main hobby: <input type="text" name="main hobby" /> </div>
<div> <input type="submit" value="Send"> </div>
</form>

<h1> <u> Results: </u> </h1>
name: %s <br/>
<div> family: %s <br/>
</html>""" % (name, family)