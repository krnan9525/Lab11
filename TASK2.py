import urllib2
import boto

p1='username'
p2='userpass'
url='http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key'

req = urllib2.Request(url)
res = urllib2.urlopen(req)
"""req.status_code"""
str1 = res.read()
p1,p2 = str1.split(':')
print p1,'\n',p2,'\n',boto.Version
