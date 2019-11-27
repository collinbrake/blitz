import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

def plot(nparray, scale=1, title="Plot"):

    # Scale the image as specified
    nparray = cv.resize(nparray, None, fx=scale, fy=scale,
                    interpolation=cv.INTER_CUBIC)

    # Define the axis based on the image size
    xlen, ylen = nparray.shape
    x = np.linspace(0, xlen, xlen)
    y = np.linspace(0, ylen, ylen)
    X, Y = np.meshgrid(y, x)

    # Plot the image
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, nparray, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_title(title)
