#Customize the colours of the logo

###What is this?

Allow users to customize each school page by allowing them to select colours for the CSS as well as a custom logo.  

###Inputs

####RGB
If you have rgb (red, green, blue) colour values, follow this scheme of inputs:

* top: `int r1`,`int g1`, `int b1`
* sides: `int r2`,`int g2`, `int b2`
* middle: `int r3`,`int g3`, `int b3`
* background: `int r4`,`int g4`, `int b4`

`changePicRGB(r1,g1,b1, r2,g2,b2, r3,g3,b3, r4,g4,b4)`

*Note: if you want to leave the dark black line, make background = `35, 31, 32`*

####Hex

If you have hex (#123456) colour values, follow this scheme of inputs:

* `str top`
* `str sides`
* `str middle`
* `str background`

`changePicHex(top, sides, middle, background)`

*Note: if you want to leave the dark black line, make background = `#231F20`*
