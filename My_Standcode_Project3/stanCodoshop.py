"""
File: stanCodoshop.py
Name: Stephanie
----------------------------------------------
This program is SC101 Assignment 3 and is adapted
from Nick Parlante's Ghost assignment.

The assignment has been redesigned and extended
by Jerry Liao to fit the learning objectives of
the stanCode SC101 course.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Computes the Euclidean color distance between a pixel's RGB values and a target mean RGB color.

    This function measures how similar a pixel is to a reference color by treating the
    red, green, and blue channels as coordinates in a 3D color space. A smaller distance
    indicates a closer color match.

    Parameters:
        pixel (Pixel): The pixel whose RGB components (pixel.red, pixel.green, pixel.blue)
            will be compared.
        red (int): The reference mean red value.
        green (int): The reference mean green value.
        blue (int): The reference mean blue value.

    Returns:
        float: The Euclidean distance between the pixel's RGB values and the reference color.
    """
    sqr = (red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2
    color_distance = sqr ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # initization
    total_red = 0
    total_green = 0
    total_blue = 0

    # each loop to get sum of R, G, B
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue

    # get avg value of R, G, B (must get int)
    n = len(pixels)
    return [total_red // n, total_green // n, total_blue // n]


def get_best_pixel(pixels):
    """
    Selects the pixel that is closest in color to the average color of a group of pixels.

    This function examines a list of pixels and determines which one has the smallest
    color distance to the average RGB values of all pixels in the list. It is useful
    for finding the most "representative" pixel in a set.

    Parameters:
        pixels (List[Pixel]): A list of Pixel objects to evaluate.

    Returns:
        Pixel: The pixel whose color is closest to the average color of the input list.
    """
    # get average value of R, G, B
    avg_rgb_lst = get_average(pixels)
    avg_red = avg_rgb_lst[0]
    avg_green = avg_rgb_lst[1]
    avg_blue = avg_rgb_lst[2]

    # 2. initization
    best_pixel = None
    min_dist = 99999  # assume min_dist a large number as root for comparing

    # to compare dist with min_dist to get the best pixel
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)
        if dist < min_dist:
            min_dist = dist
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display the solution image
    based on images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # To get every pixel's x, y of every image, and append in pixels list
    for x in range(width):
        for y in range(height):
            pixels = []
            for img in images:
                pixels.append(img.get_pixel(x, y))

            # find the best dist pixel
            best_pixel = get_best_pixel(pixels)

            # 3. replace the pixel of blank image with best_pixel
            final_pixel = result.get_pixel(x, y)
            final_pixel.red = best_pixel.red
            final_pixel.green = best_pixel.green
            final_pixel.blue = best_pixel.blue


    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
