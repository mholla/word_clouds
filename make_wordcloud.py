import numpy as np
from PIL import Image
from os import path
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
from webcolors import *
from wordcloud import WordCloud, STOPWORDS


def make_cmap(colors, position=None, bit=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.

    courtesy of http://schubert.atmos.colostate.edu/~cslocum/custom_cmap.html
    '''

    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return cmap

def create_cmap():

    # define desired colors
    fluid = name_to_rgb('dodgerblue')
    black = name_to_rgb('black')
    gray1 = name_to_rgb('dimgray')
    gray2 = name_to_rgb('gray')
    gray3 = name_to_rgb('darkgray')
    gray4 = name_to_rgb('silver')
    white = name_to_rgb('lightgray')

    # compile colors into a colormap
    mode_colors = [black, gray1, gray2, gray3, gray4, fluid, white]
    colormap = make_cmap(mode_colors, bit=True)

    # discretize (from https://gist.github.com/jakevdp/91077b0cae40f8f8244a)
    N = 7
    base = plt.cm.get_cmap(colormap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    colormap = base.from_list(cmap_name, color_list, N)

    # to visualize your color map, uncomment the lines below
    # plt.pcolor(np.random.rand(25,50), cmap=colormap)
    # plt.colorbar()
    # plt.show()

    return colormap

def preprocess_text(textfilename):

    text = open(textfilename, encoding='utf-8').read()

    # preprocess the text as needed
    text = text.replace("thicknesses", "thickness")
    text = text.replace("stiffnesses", "stiffness")
    text = text.replace("stiff ", "stiffness ")
    text = text.replace("sulci", "sulcal")
    text = text.replace("gyri ", "gyral ")
    text = text.replace("film ", "layer ")
    text = text.replace("thickest", "thick")
    text = text.replace("modeling", "model")

    # # add specific stopwords
    stopwords = set(STOPWORDS)
    stopwords.add("one")
    stopwords.add("two")
    stopwords.add("three")
    stopwords.add("eight")
    stopwords.add("fig")
    stopwords.add("figure")
    stopwords.add("eq")
    stopwords.add("table")
    stopwords.add("may")
    stopwords.add("non")
    stopwords.add("also")
    stopwords.add("zero")
    stopwords.add("0mm")
    stopwords.add("00mm")
    stopwords.add("red")
    stopwords.add("blue")
    stopwords.add("well")
    stopwords.add("particularly")
    stopwords.add("even")
    stopwords.add("shown")
    stopwords.add("Section")
     
    return text, stopwords

def make_wordcloud(text, stopwords, figurefilename, colormap, font_path, background_color):
    
    if colormap == 'custom': # to use your own custom colormap
        colormap = create_cmap() 

    wc = WordCloud(stopwords=stopwords,
                   # font_path=font_path,
                   prefer_horizontal=1,
                   # max_words=80,
                   width=1000,
                   height=500,
                   margin=10,
                   min_font_size=8,
                   # max_font_size=64,
                   background_color=background_color,
                   relative_scaling=0.5,
                   colormap=colormap,
                   normalize_plurals=True,
                   collocations=False,
                   random_state=1).generate(text)

    plt.imshow(wc, interpolation="bilinear")
    wc.to_file(figurefilename)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':

    textfilename = 'cleaned_up_text.txt'
    figurefilename = "word_cloud.png"
    colormap = 'custom' # or an existing colormap name like 'viridis'
    font_path = '../resources/Garamond.ttf'
    background_color = 'white'

    [text, stopwords] = preprocess_text(textfilename)
    make_wordcloud(text, stopwords, figurefilename, colormap, font_path, background_color)

     

