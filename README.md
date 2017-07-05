# condsamisistemas
A script that checks if a condominium bill is listed

The samisistemas don't send notifications via email when a bill is added to the system. So I wrote this litte script that checks whenever a bill is added, and send an email to the customer. I tested with Nova Era real state, because it's the only one I have, 
but I guess it can work with any other real states. Just get the variable 'sigla' from the URL and add it to the code.

To use it you need to set the variables:
* usuario
* senha
* email_to
* email_from

Add the script to your crontab and wait it notificate you. ;)

I suggest to run the script everyday at night, so when you got home can download the bill and pay via online banking. 
