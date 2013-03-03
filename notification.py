#!/usr/bin/env python
# Simple notification catch script for Adyen notifications
# This script just logs all incoming requests in a file

from datetime import datetime
import cgi, os

notificationdata = "/tmp/notification.data"

# Log to file in /tmp in case of errors
import cgitb
cgitb.enable(display=0, logdir="/tmp", format="text")

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

# FieldStorage to ordinary dictionary
def fs2dict(fs):
        result = {}
        for key in fs.keys():
                result[key] = fs[key].value
        return result

# Form data posted by Adyen.
# Fields: [merchantAccountCode,merchantReference,success,pspReference,value,currency,live,eventCode,paymentMethod,eventDate]

form = fs2dict(cgi.FieldStorage())

with open(notificationdata,"a") as f:
        f.write("-"*80 + "\n")
        f.write("Adyen Notification Call Received at %s\n" % datetime.now().strftime("%Y-%m-%d %H:%M:%s"))

        # Print Adyen parameters
        for key in form:
                f.write("%s: %s\n" % (key,form[key]))

        f.write("\n")

        # If you want to include the standard CGI variables in the log
        for key in os.environ.keys():
                f.write("%s: %s\n" % (key,os.environ[key]))
        f.close()
print "[accepted]"
