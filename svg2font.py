import fontforge
import os

font = fontforge.open('blank.sfd')

directory = "./svg"
    
for filename in os.listdir(directory):
    if filename.endswith(".svg"): 
        clearname = filename.split(".svg")[0]
        glyph = font.createChar(int(clearname))
        glyph.importOutlines(''+ directory + "/" + filename)
        glyph.right_side_bearing = int(glyph.left_side_bearing)
        continue
    else:
        continue


font.generate('testfont.ttf')