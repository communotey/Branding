import xml.etree.ElementTree as ET
from os.path import exists

# image libraries use rgb, not hex, but some people may want to input hex
def rgb2Hex(r,g,b):    
    rh = hex(r)
    gh = hex(g)
    bh = hex(b)
    
    #hex values need to be 2 characters each
    if len(rh)<4:
        rh = "0"+rh[2:]
    else:
        rh = rh[2:]
        
    if len(gh)<4:
        gh = "0"+gh[2:]
    else:
        gh = gh[2:]
        
    if len(bh)<4:
        bh = "0"+bh[2:]
    else:
        bh = bh[2:]
    
    hexColour = "" + rh + gh + bh
    return hexColour

#######################################
def changeTree(top, sides, background):
    tree = ET.parse("triangle_empty.svg")
    ET.register_namespace("","http://www.w3.org/2000/svg")
    for element in tree.iter():
        if element.get('id') == 'sides':
            element.set('fill', sides)
            element.set('stroke', background)

        elif element.get('id') == 'bottom':
            element.set('fill', top)        #make top/bottom same colour
            element.set('stroke', background)

        elif element.get('id') == 'top':
            element.set('fill', top)
            element.set('stroke', background)
    return tree

#########################################################
#if given rgb, you have to convert it to hex and it's fun
def changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3):
    top = rgb2Hex(r1,g1,b1)  #top
    sides = rgb2Hex(r2,g2,b2)  #sides
    background = rgb2Hex(r3,g3,b3)  #line should be your background colour
    
    path = "triangle_"+top+ "_"+sides+"_"+background+".svg"
    if exists(path):
        #if this is true, the file exists; no reason to make another
        print "The image exists"
    else:
        #make another
        print "Creating image..."

        #I only left them in there to make the path
        top = "#" + top
        sides = "#" + sides
        background = "#" + background

        tree = changeTree(top, sides, background)
        tree.write(path)
        
        
##################################################
#if given the hex values, deal with the hex values
def changePicHex(top, sides, background):

    #lower case for standards sake
    top = top.lower()
    sides = sides.lower()
    background = background.lower()
    
    #cut out the hash
    path = "triangle_"+top[1:]+ "_"+sides[1:]+"_"+background[1:]+".svg"
    if exists(path):
        #if this is true, the file exists; no reason to make another
        print "The image exists"
    else:
        #make another
        print "Creating image..."

        #no need to add the hash back because it was never removed 
        tree = changeTree(top, sides, background)
        tree.write(path)

###################################################
#uncomment the next 13 lines if you have RGB values
#r1=142
#g1=151
#b1=157

#r2=122
#g2=0
#b2=60

#r3=255
#g3=255
#b3=255

#changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3)

##################################################
#uncomment the next 5 lines if you have HEX values
#top="#fdBF57"
#sides="#193989"
#background="#231F20"

#changePicHex(top,sides,background)
