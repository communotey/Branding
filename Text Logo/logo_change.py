import xml.etree.ElementTree as ET
from os.path import exists

# image libraries use rgb, not hex, but some people may want to input hex
def rgb2Hex(r,g,b):    
    rh = hex(r)
    gh = hex(g)
    bh = hex(b)
    hexColour = ""+rh[2:] + gh[2:] + bh[2:]
    return hexColour

###############################################
def changeTree(top, sides, middle, background):
    tree = ET.parse("triangle_empty.svg")
                    
    for element in tree.iter():
        if element.get('id') == 'sides':
            element.set('fill', sides)
            element.set('stroke', background)

        elif element.get('id') == 'middle':
            element.set('fill', middle)
            element.set('stroke', background)

        elif element.get('id') == 'top':
            element.set('fill', top)
            element.set('stroke', background)
    return tree

#########################################################
#if given rgb, you have to convert it to hex and it's fun
def changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3, r4,g4,b4):
    top = rgb2Hex(r1,g1,b1)  #top
    sides = rgb2Hex(r2,g2,b2)  #sides
    middle = rgb2Hex(r3,g3,b3)  #middle
    background = rgb2Hex(r4,g4,b4)  #line should be your background colour
    
    path = "triangle_"+top+ "_"+sides+"_"+middle+"_"+background+".svg"
    if exists(path):
        #if this is true, the file exists; no reason to make another
        print "The image exists"
    else:
        #make another
        print "Creating image..."

        #I only left them in there to make the path
        top = "#" + top
        sides = "#" + sides
        middle = "#" + middle
        background = "#" + background

        tree = changeTree(top, sides, middle, background)
        tree.write(path)
        
        
##################################################
#if given the hex values, deal with the hex values
def changePicHex(top, sides, middle, background):

    #cut out the hash
    path = "triangle_"+top[1:]+ "_"+sides[1:]+"_"+middle[1:]+"_"+background[1:]+".svg"
    if exists(path):
        #if this is true, the file exists; no reason to make another
        print "The image exists"
    else:
        #make another
        print "Creating image..."

        #no need to add the hash back because it was never removed 
        tree = changeTree(top, sides, middle, background)
        tree.write(path)

r1=123
g1=22
b1=202

r2=202
g2=123
b2=22

r3=123
g3=202
b3=22

r4=22
g4=202
b4=123

changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3, r4,g4,b4)
