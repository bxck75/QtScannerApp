import sys,os
from optparse import OptionParser
import inspect


class Tools:
    
    def __init__(self):
        
        print('HelperClass init....')
        # print(locals()['Helper'])
        # print(globals()['Helper'])

    def saveFile(self,file,textfield):
        # print('HelperClass saveFile method called')     
        # print(textfield.toPlainText())
        f = open(file, 'w')
        filedata = textfield.toPlainText()
        filedata = str(filedata)+"\n"
        f.write(filedata)
        f.close()
        print('file '+file+' Saved!')
           
    def InspectM(self,target):
        print(target)
        #print(inspect.getmembers(target, predicate=inspect.ismethod))
        for m in inspect.getmembers(target, predicate=inspect.ismethod):
            name,value = m
            
            if name != '__init__':
                print('--- '+name)

    def InspectC(self,target):
        print(target)
        #print(inspect.getmembers(target, predicate=inspect.ismethod))
        for m in inspect.getmembers(target, predicate=inspect.isclass):
            name,value = m
            
            if name != '__init__':
                print('--- '+name)

    def WriteListToFile(self):
    
        file = open('testfile.txt','w')     
        file.write('Hello World') 
        file.write('This is our new text file') 
        file.write('and this is another line.') 
        file.write('Why? Because we can.') 
        file.close()

    def ReadListFromFile(self,file):
        print('HelperClass ReadListFromFile method called on '+file) 
        file = open(file, 'r') 
        lines = []
        for line in file:
            if line != '':
                lines += line.strip(),
        return lines

class Die:
    def __init__(self):
        print('Exiting....')
        sys.exit()