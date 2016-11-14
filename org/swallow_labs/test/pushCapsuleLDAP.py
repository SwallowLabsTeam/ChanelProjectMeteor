'''Script to instance a client stub and push two capsule'''
from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
import sys
# get argument (JSON) and manipulate it
jsonObj = sys.argv[1]
print(" Object received : "+jsonObj)
operation,dn,userType,AAssigningContent,ADashboradGA,AInvoiceGA,AContartGA,AClientGA,AScreensGA,ASegmentGA,ABookingGA,AAccountGA,email,password,fname,surname,cin,dateOfBirth,phone,address = jsonObj.split("*")
print ("DN :",dn)
print ("Operation :",operation)
print ("userType :",userType)
print ("AAssigningContent :",AAssigningContent)
print ("ADashboradGA :",ADashboradGA)
print ("AInvoiceGA :",AInvoiceGA)
print ("AContartGA :",AContartGA)
print ("AClientGA :",AClientGA)
print ("AScreensGA :",AScreensGA)
print ("ASegmentGA :",ASegmentGA)
print ("ABookingGA :",ABookingGA)
print ("AAccountGA :",AAccountGA)
print ("email:",email)
print ("password :",password)
print ("fname :",fname)
print ("surname :",surname)
print ("cin :",cin)
print ("dateOfBirth :",dateOfBirth)
print ("phone :",phone)
print ("address :",address)

l = Parser.get_backend_broker_list()
c = Client(5, l)
print("client launched")
capsule = Capsule(c.id_client, CapsuleType.PAYLOAD)
capsule.set_sort(CapsuleSort.LDAP_ADD_MSG)
if userType == "admin":
    if operation == "add":
        print("I am here")
        capsule.set_payload({'att':['dn','objectClass','AEmail','AFirstName','ALastName','AAdress','APassword','ATelephone','ADateOfBirth','APicture','ACIN','AAssigningContent','ADashboradGA','AInvoiceGA','AContartGA','AClientGA','AScreensGA','ASegmentGA','ABookingGA','AAccountGA'],'dn': dn,'objectClass': ['top','AppAdministrator'],'AEmail': email,'AFirstName': fname,'ALastName': surname,'AAdress': address,'APassword': password,'ATelephone': phone,'ADateOfBirth': dateOfBirth,'APicture': '/home/userPictures/1001/','ACIN': cin, 'AAssigningContent':AAssigningContent,'ADashboradGA':ADashboradGA,'AInvoiceGA':AInvoiceGA,'AContartGA':AContartGA,'AClientGA':AClientGA,'AScreensGA':AScreensGA,'ASegmentGA':ASegmentGA,'ABookingGA':ABookingGA,'AAccountGA':AAccountGA})
        capsule.set_id_receiver("20")
        capsule.set_priority(CapsulePriority.LDAP_ADD)
if userType == "client":
    print("It's client user")
c.generate()
if c.push(capsule) == 1:
    print("Capsule Sent")
