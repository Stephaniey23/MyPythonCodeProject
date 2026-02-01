"""
File: blur.py
Name: Stephanie
-------------------------------
This program first displays the original image,
smiley-face.png, and then compares it with a
blurred version of the image.

The blur effect is created by replacing each
pixel with the average RGB values of its
nearest neighboring pixels.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original picture
    :return: the blurred picture
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            # initization
            total_r = 0
            total_g = 0
            total_b = 0
            count = 0

            for i in range(x - 1, x + 2):
                # Inclusive of start, Exclusive of stop, so the range is from x-1 to x+2
                for j in range(y - 1, y + 2):
                    # check the boarder to make sure the pixel within the range
                    if 0 <= i < img.width and 0 <= j < img.height:
                        pixel = img.get_pixel(i, j)
                        total_r += pixel.red
                        total_g += pixel.green
                        total_b += pixel.blue
                        count += 1

            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = total_r // count
            new_pixel.green = total_g // count
            new_pixel.blue = total_b // count

    return new_img


def main():
    """
    TODO : Blurred the original picture
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
