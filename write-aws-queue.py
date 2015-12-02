# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

p1='username'
p2='userpass'
url='http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'


# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = ""
secret_access_key = ""
url='http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'

req = urllib2.Request(url)
res = urllib2.urlopen(req)
"""req.status_code"""
str1 = res.read()
access_key_id,secret_access_key = str1.split(':')
print access_key_id,'\n',secret_access_key

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Get a list of the queues that exists and then print the list out

str2=raw_input("input the queue name:")
queue1 = conn.get_queue(str2)
str3=raw_input("input the message:")
m = Message()
m.set_body(str3)
queue1.write(m)
print 'message sent'
#print(response.get('MessageId'))
#print(response.get('MD5OfMessageBody'))
