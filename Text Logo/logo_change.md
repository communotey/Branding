#Customize the colours of the logo

###What is this?

Allow users to customize the logo colours to match those of each school.  

###How to use this?

It will soon be on the website, but until then:

1. Put the `triangle_empty.svg` file in the same folder that you downloaded the python script
2. Put your values at the bottom of the script, where instructed 

###Inputs

####RGB
If you have rgb (red, green, blue) colour values (0-255), follow this scheme of inputs:

* top/bottom: `int r1`,`int g1`, `int b1`
* sides: `int r2`,`int g2`, `int b2`
* background: `int r4`,`int g4`, `int b4`

`changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3, r4,g4,b4)`

*Note: if you want to leave the dark black line, make background = `35, 31, 32`*

####Hex

If you have hex (#231f20) colour values, follow this scheme of inputs:

* top/bottom: `str top`
* sides: `str sides`
* background: `str background`

`changePicHex(top, sides, background)`

*Note: if you want to leave the dark black line, make background = `#231f20`*
