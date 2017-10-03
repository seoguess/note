#!/usr/bin/env python
#coding: utf-8

a = "this is %s and %s"
print a  % ('shawn', 'lowkey')

b = "this is {} and {}"

print b .format ('shawn','lowkey')

c = "this is {shawn} and {lowkey}"
print c .format (shawn='shawn',lowkey='lowkey')


d = "this is %(shawn)s and %(lowkey)s"
print d % {'shawn':'shawn','lowkey':'lowkey'}

