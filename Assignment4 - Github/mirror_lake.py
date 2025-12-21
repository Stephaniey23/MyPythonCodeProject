"""
File: mirror_lake.py
Name: Stephanie
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: mirror_lake (the original )
    :return: the original + the reversed one
    """
    # return 0
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            imgp = img.get_pixel(x, y)
            bp1 = b_img.get_pixel(x, y)
            bp1.red = imgp.red
            bp1.green = imgp.green
            bp1.blue = imgp.blue
            bp2 = b_img.get_pixel(x,b_img.height-1-y)
            bp2.red = imgp.red
            bp2.green = imgp.green
            bp2.blue = imgp.blue
    return b_img


def main():
    """
    TODO: To create the new photo including the original mirror_lake and its reversed one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
