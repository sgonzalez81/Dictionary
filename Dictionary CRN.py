# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 00:28:06 2022

@author: salva
For this exercise, write a dictionary that catalogs the classes you took last term - the keys should be the class CRN number (without the 'CRN' part), and the values should be the title of the class.


Then, write a function 'add class' that takes 2 arguments - a class number and a description - and adds the class to your dictionary.  Use this function to add the classes you’re taking this term to the dictionary.


Finally, write a function print classes that takes one argument - a Course CRN number  - and prints out all the classes you took in that have that CRN or a smaller CRN.


Example output:


>> print_classes(’77693’)


Introduction to Python

 

if you input a CRN that is not in your dictionary, say 
>> print_classes(’99999’) The print the message: 

No Course 99999 classes taken.
"""
classes = {}

def add_class(crn, name):
    classes[crn] = name

def print_classes(crn):
    if crn in classes:
        print(f'[CRN:{crn}] - {classes[crn]}')
    else:
        print(f'No course {crn} is being taken this semester.')


# Fall 2021
add_class(77692, 'CIS161 - Introduction to C Programming')
add_class(77889, 'CA131 - Relational Database Management')
add_class(77691, 'CIS113 - Data Structures')
add_class(77896, 'CA151 - 	Microcomputer Operating System')

# Spring 2022
add_class(36753, 'BIOL104 - Environmental Biology')
add_class(36729, 'HD101 - College and Life Management')
add_class(77697, 'CIS121 - Computer Mathematics')
add_class(77896, 'MUSC108 - History of Hip Hop')

# Summer 2022
add_class(77673, 'HIST108 - U.S. History from 1865')
add_class(77623, 'MATH115 - Statistics')

# Fall 2022
add_class(77693, 'CIS177 - Introduction to Python')
add_class(77896, 'CA151 - Microcomputer Operating System')
add_class(77697, 'CIS121 - 	Computer Mathematics')



# Example of displaying classes ive taken this semester
print('Classes taken in fall 2022:')
print_classes(77693)
print_classes(77896)
print_classes(77697)


# Print a non-existant class test case
print('\n\nNon-existant class test case:')
print_classes(1)
