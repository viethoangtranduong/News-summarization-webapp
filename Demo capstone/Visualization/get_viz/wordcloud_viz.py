from wordcloud import WordCloud, STOPWORDS
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def wordcloud_viz(txt, name):
    """plot word cloud

    Args:
      txt (str): text for plot
      name (str) file name

    Returns:
      file location
    """  
    txt = txt.lower()
    mpl.rcParams['font.size']=12                #10
    mpl.rcParams['savefig.dpi']=100             #72
    mpl.rcParams['figure.subplot.bottom']=.1

    # get stopwords to remove
    stopwords = set(STOPWORDS)

    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        random_state=42
        ).generate(txt)

    plt.figure(figsize=(20,20))
    plt.imshow(wordcloud)
    plt.axis('off')
    # plt.show()

    
    # if pythonanywhere, use the following url
    # plt.savefig(f"/home/viethoangtranduong/xlite_capstone/static/image_output/{name}_most_frequent_viz.png", dpi=500) 
    
    # if not pythonanywhere
    plt.savefig(f"{name}_wordcloud_viz.jpg", dpi=500)
    print("done wc", f"{name}_wordcloud_viz.png")
    return f"{name}_wordcloud_viz.jpg"

    