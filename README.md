# condsamisistemas
A script that checks if a condominium bill is listed

The samisistemas don't send notifications via email when a bill is added to the system. So I wrote this litte script that checks whenever a bill is added, and send an email to the customer.

To use it you need to set the variables:
* usuario
* senha
* email_to
* email_from

Add the script to your crontab and wait it notificate you. ;)

I suggest to run the script everyday at night, so when you got home can download the bill and pay via online banking. 
