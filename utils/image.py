from PIL import Image
import os


def cropimage(sourceurl='', cropwidth=225, cropheight=225, destinationurl=''):
    Image.MAXIMAGEPIXELS = None
    image = Image.open(sourceurl)
    imagewidth, imageheight = image.size

    if imagewidth < cropwidth and cropwidth < cropheight:
        image = image.resize((cropwidth, imageheight))
    if imageheight < cropheight and cropwidth > cropheight:
        image = image.resize((cropwidth, cropheight))

    primarycroppedimage = image

    cropedimage = primarycroppedimage.resize((cropwidth, cropheight))

    if destinationurl == '':
        sourceurldetails = os.path.splitext(sourceurl)
        destinationurl = sourceurldetails + '' + \
            str(cropwidth) + 'x' + str(cropheight) + sourceurldetails[1]

    cropedimage.save(destinationurl)
    return destinationurl
