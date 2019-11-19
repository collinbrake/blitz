import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def plot(img_file):
    # Read the image
    img = cv.imread(img_file, 0)

    # Define the axis based on the image size
    xlen, ylen = img.shape
    x = np.linspace(0, xlen, xlen)
    y = np.linspace(0, ylen, ylen)
    X, Y = np.meshgrid(y, x)

    # Plot the image
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, img, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_title(img_file)
