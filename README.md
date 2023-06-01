# word_clouds
generating beautiful word clouds from text, as seen on [my publications page](https://commandlab.nd.edu/publications/)

## Setup (Mac)
1. set up DeTeX (for LaTeX)
    - put [this file](https://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-1.0/lib/texmf/web2c/texmf.cnf) in `/usr/local/bin`
    - download and unzip [opendetex](https://github.com/pkubowicz/opendetex/)
    - follow instructions in INSTALL: `sudo make install`
    - copy folder to Applications
2. install required packages: 
    - `pip install -r requirements.txt`

## Making word clouds (Mac)
1. Preprocess source file: 

    If you're starting with a LaTeX file (probably also true for other files) you will want to clean it up first: 
    - use regular expressions (e.g. `\\autocite\{.{5, 50}\})` or manual searching to clean up some parts that detex doesn't handle well (`textcite`, `autoref`, `label`, `cite`, `citep`, etc.)
    - use detex to clean up a lot of the rest: `detex input.tex > output.tex`
    - then delete title, equations, tables, etc. as desired
    
    An example of the text I use for word clouds is included here as `cleaned_up_text.txt`
2. Set up fonts 

    If you want to use a font other than the default (DroidSansMono.ttf), you must: 
    - download your [desired fonts](https://fonts.google.com/) to a nearby folder 
    - update the font_path name in `make_wordcloud.py`
    - uncomment the `font_path = font_path` option in the WordCloud command
4. Customize options
    - set the `textfilename` and `figurefilename` paths in the `make_wordcloud.py` file
    - set the background color and a color map for the words (or optional: create a custom color map by defining a few colors in `create_cmap`)
    - optional: add or remove stopwords or replacements in `preprocess_text` (I usually do this iteratively after making the wordcloud and seeing things like Fig. or thicknesses on there)
5. Run!  `python make_wordcloud.py`

## Custom color maps
If you want to use an existing color map, it's easy.  But often I want to use specific, discrete colors, so I make my own color map, using the `create_cmap` function, in which you 
1. define your colors (from a name `gray1 = name_to_rgb('dimgray')`, from hex `purple = hex_to_rgb('#9437FF')`, etc.)
2. compile all your colors into a colormap
3. discretize into distinct colors

## Acknowledgements 
This project was inspired by Ben Haller's [publication word clouds](http://benhaller.com/wordclouds.html) and a [thesis tag cloud](http://ocam.cl/a-tag-cloud-of-my-thesis.html) (link broken) and draws heavily from [Andreas Mueller's word cloud generator](https://github.com/amueller/word_cloud).

It also makes use of code/snippets from [Chris Slocum](http://schubert.atmos.colostate.edu/~cslocum/custom_cmap.html) and [Jake Vanderplas](https://gist.github.com/jakevdp/91077b0cae40f8f8244a) for custom colormaps.
