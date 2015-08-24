from os.path import exists
import xml.etree.ElementTree as ET
ET.register_namespace("","http://www.w3.org/2000/svg")

###############################################################
# css uses hex, not rgb, but some people may want to input rgb
def rgb2Hex(r,g,b):    
    rh = hex(r)
    gh = hex(g)
    bh = hex(b)
    
    #hex values need to be 2 characters each, but 0-A is only 1 character
    if len(rh)<4:
        rh = "0"+rh[2:] #[2:] gets rid of the 0x
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
    
    hexColour = "#" + rh + gh + bh
    return hexColour

###############################################
# where the action happens
def changeTree(top, sides, bottom):

    #cut out the hash
    path = "triangle_"+top[1:]+"_"+sides[1:]+"_"+bottom[1:]+".svg"
    if exists(path):
        #if this is true, the file exists; no reason to make another
        print "The image exists"
    else:
        #make another
        print "Creating image..."
        
        tree = ET.parse("triangle_empty.svg")
        for element in tree.iter():
            if element.get('id') == 'sides':
                element.set('fill', sides)

            elif element.get('id') == 'bottom':
                element.set('fill', bottom)

            elif element.get('id') == 'top':
                element.set('fill', top)

        tree.write(path)

##########################################################
# if given rgb, you have to convert it to hex and it's fun
def changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3):
    top = rgb2Hex(r1,g1,b1)
    sides = rgb2Hex(r2,g2,b2)
    bottom = rgb2Hex(r3,g3,b3)
        
    tree = changeTree(top, sides, bottom)
        
#########################################
# if given the hex values, keep it in hex
def changePicHex(top, sides, bottom):

    #lower case for standards sake
    top = top.lower()
    sides = sides.lower()
    bottom = bottom.lower()

    tree = changeTree(top, sides, bottom)

###################################################
#uncomment the next 13 lines if you have RGB values
#r1=142
#g1=151
#b1=157

#r2=122
#g2=0
#b2=60

#r3=142
#g3=151
#b3=157

#changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3)

##################################################
    
top="#fdBF57"
sides="#193989"
bottom="#fdBF57"

changePicHex(top,sides,bottom)
