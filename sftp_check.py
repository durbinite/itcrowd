#! /usr/bin/env python
# Usage: pysftp <hostname> <port> <username> <password> <connect_timeout>
#

import pysftp
import sys

if len(sys.argv) != 6:
  print "Wrong number of arguments, verify check configuration!"
  sys.exit(1)

try:
  hostname = sys.argv[1]
  port = int(sys.argv[2])
  username = sys.argv[3]
  password = sys.argv[4]
  timeout = int(sys.argv[5])
except Exception as e:
  print "Could not parse arguments, verify check configuration!"
  sys.exit(1)

try:
  print "Connecting to {0}:{1} (timeout {2} sec)...".format(hostname, port, timeout)
  sftp_connection = SFTP()
  sftp_connection.connect(hostname, port, timeout)
except Exception as e:
  print "Could not connect to server. {0}".format(e)
  sys.exit(1)

sftp_connection.set_debuglevel(1)

try:
  print "Trying to log in with username \"{0}\"...".format(username)
  sftp_connection.login(username, password)
except Exception as e:
  print "Failed to log in with specified credentials. {0}".format(e)
  sys.exit(1)

try:
  print "Getting welcome message from server..."
  sftp_connection.getwelcome()
except Exception as e:
  print "Failed to get welcome message from server. {0}".format(e)
  sys.exit(1)

sftp_connection.quit()
