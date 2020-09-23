import cv2
import numpy as np
import matplotlib.pyplot as plt

def plotHist(name, hist):
    squeeze = np.squeeze(hist)
    plt.plot(squeeze)
    plt.title(name)
    plt.show()

def calcHist(image):
    hist = np.zeros(256)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            hist[image[x][y]] += 1
    return hist

def calcLuminance(image):
    imageL = 0.299*image[:,:,2] + 0.587*image[:,:,1] + 0.114*image[:,:,0]
    return np.uint8(imageL)

def compareHist(image):
    histL = calcHist(calcLuminance(image))

    histB = calcHist(imageC[:, :, 0])
    histG = calcHist(imageC[:, :, 1])
    histR = calcHist(imageC[:, :, 2])

    h = 0.299*histR + 0.587*histG + 0.114*histB
    plotHist("Histogram of L", histL)
    plotHist("Histogram of h", np.uint8(h))

if __name__ == '__main__':
    # read gray and color image
    imageG = cv2.imread('img.png', 0)
    imageC = cv2.imread('img.png')

    # calc and show histogram
    histG = calcHist(imageG)

    histB = calcHist(imageC[:,:,0])
    histG = calcHist(imageC[:,:,1])
    histR = calcHist(imageC[:,:,2])

    plotHist("Histogram of image G", histG)

    plotHist("Histogram of image C, channel B", histB)
    plotHist("Histogram of image C, channel G", histG)
    plotHist("Histogram of image C, channel R", histR)

    # calc luminance
    plt.imshow(calcLuminance(imageC), cmap='gray')
    plt.title("Luminance of image imageC ")
    plt.show()

    # Histogram hL and histogram h are diffrents
    compareHist(imageC)