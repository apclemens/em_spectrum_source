from freqToRGB import freqToRGB
from PIL import Image, ImageDraw

WIDTH = 500

img = Image.new('RGB', (WIDTH, 1), color='red')
draw = ImageDraw.Draw(img)
startFreq = 4.283e14
endFreq = 7.495e14
for x in range(WIDTH):
    freq = startFreq**((WIDTH-x)/WIDTH) * endFreq**(x/WIDTH)
    draw.point((x,0), fill=freqToRGB(freq))

img.save('visible.png', 'png')
