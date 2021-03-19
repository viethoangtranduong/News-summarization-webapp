# What's new Capstone

Website: http://viethoangtranduong.pythonanywhere.com/

**"What's new?"** is a web app to summarize information from Medium, Arxiv, and NeurIPS. If you are like me, got lost in numerous Medium or Arxiv articles, wondering which article to read. "What's new?" (WN) is here to help. WN will query and summarize the top 10+ relevant reports for you to read and understand any topic. Then, you can choose the articles you like the most. We also provide word cloud and most frequent words visualization to understand the general trends and keywords of the field, helping to stay updated with new technologies and trends.

## Structure

There are 2 versions and 3 folders:  
- (Lite version) The ```full_capstone``` includes all the functionalities.  
- (Full version) The ```xlite_capstone``` is the smaller version, with all the functionalities except the Bert summarization models (HuggingFace + Bert-extractive).  
- The ```Demo capstone``` is the Jupyter notebooks demoing every functions and its output for the web app.

The current deploying model on the website is the ```xlite_capstone``` version to maintain the efficient cost. The code structures are listed within each folder.  

The embeddings and the hgf models can be found [here](https://drive.google.com/drive/folders/1ifPOnWqUXv2f5NR8nHgdAdUwFQVr-DiO?usp=sharing).

