from moviepy.editor import *


def createImage():

    from PIL import Image, ImageDraw, ImageFont

    im = Image.new('RGB', (500, 500), color=('#2A2B2A'))

    font = ImageFont.truetype('C:/Windows/Fonts/CENTURY.TTF', size=36)

    dt = ImageDraw.Draw(im)
    dt.text(
        (20, 20),
        'a set of inputs',
        font=font,
        fill=('#EFC88B')
    )

    im.save('C:/Users/student/Documents/122А/Никитин/images/4.jpg')


def createMovie():
    c1 = ImageClip('1.jpg').set_duration(2)
    c2 = ImageClip('2.jpg').set_duration(2)
    c3 = ImageClip('3.jpg').set_duration(2)
    c4 = ImageClip('4.jpg').set_duration(2)
    c5 = ImageClip('5.jpg').set_duration(2)

    fc = concatenate_videoclips([c1, c2, c3, c4, c5], method='compose')
    fc.write_videofile('function.mp4', fps=60)
