'''
Created on 4 Oct 2013

@author: Chris
'''
import xml.dom.minidom
print ('Hello, world!')

problem_xml = """\
<?xml version="1.0" encoding="UTF-8"?>
<Problem-definition xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="problem%20definition.xsd" Name="Add">
    <Operand>+</Operand>
    <Variable Name="x" />
    <Variable Name="y" />
    <Variable Name="z" />
</Problem-definition>
"""

dom = xml.dom.minidom.parseString(problem_xml)

problemDict = {}

name_xml = dom.getElementsByTagName("Problem-definition")
name = name_xml[0].getAttribute("Name")

op_xml = dom.getElementsByTagName("Operand")
operand = op_xml[0].firstChild.nodeValue

var_xml = dom.getElementsByTagName("Variable")

i = 0

for var_name in var_xml:
    i += 1

py_expression = ''

for var_name in var_xml:
    i -= 1
    py_expression += var_name.getAttribute("Name")
    if i != 0:
        py_expression += operand

problemDict[name] = py_expression

print (name)
print (operand)
print (py_expression)
print (problemDict)

problem_xml = """\
<?xml version="1.0" encoding="UTF-8"?>
<Problem-definition xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="problem%20definition.xsd" Name="DoubleAdd">
    <Operand>+</Operand>
    <Variable Name="x" />
    <Variable Name="y">Add</Variable>
</Problem-definition>
"""

dom = xml.dom.minidom.parseString(problem_xml)

name_xml = dom.getElementsByTagName("Problem-definition")
name = name_xml[0].getAttribute("Name")

op_xml = dom.getElementsByTagName("Operand")
operand = op_xml[0].firstChild.nodeValue

var_xml = dom.getElementsByTagName("Variable")
variables = {}

for var_name in var_xml:
    i += 1
    n = 0

py_expression = ''

for var_name in var_xml:
    i -= 1
    node = ''

    try:
        node = var_xml[n].firstChild.nodeValue

    except:
        pass

    if node != '':
        py_expression += '(' + problemDict[var_xml[n].firstChild.nodeValue] + ')'

    else:
        py_expression += var_name.getAttribute("Name")

    n += 1
    if i != 0:
        py_expression += operand

problemDict[name] = py_expression
print (name)
print (operand)
print (problemDict)
    
