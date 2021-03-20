# What's new Capstone

Website: http://viethoangtranduong.pythonanywhere.com/

**"What's new?"** is a web app to summarize information from Medium, Arxiv, and NeurIPS. If you are like me, got lost in numerous Medium or Arxiv articles, wondering which article to read. "What's new?" (WN) is here to help. WN will query and summarize the top 10+ relevant reports for you to read and understand any topic. Then, you can choose the articles you like the most. We also provide word cloud and most frequent words visualization to understand the general trends and keywords of the field, helping to stay updated with new technologies and trends.

## Structure

There are 2 versions and 3 folders:  
- (Full version) The ```full_capstone``` includes all the functionalities.  
- (Xlite version) The ```xlite_capstone``` is the smaller version, with all the functionalities except the Bert summarization models (HuggingFace + Bert-extractive).  
- The ```Demo capstone``` is the Jupyter notebooks demoing every functions and its output for the web app.

The current deploying model on the website is the Xlite version (```xlite_capstone```) to maintain the efficient cost. The code structures are listed within each folder.

The embeddings and the hgf models can be found [here](https://drive.google.com/drive/folders/1ifPOnWqUXv2f5NR8nHgdAdUwFQVr-DiO?usp=sharing).

## Recommendations
- If you want to run the lite version web app, access the ```xlite_version``` folder and follow the ```README.md``` file there. The file should guide you-  through running the code.
- If you want to run the full version web app, access the ```full_version``` folder and follow the ```README.md file```. The file should guide you through running the code.
- If you want to know the web app's functions and what they are supposed to output, or to see the model comparison, then use the ```Demo capstone``` and use the ```README.md``` there. If you want to run the ```Demo capstone```, I prepared a Google Drive folder with the Colab Notebooks to run these Jupyter Notebooks. This way, you can save time for installations and make sure all the versions are compatible. Also, it can save your computational power compared to if you run them locally.[Link](https://drive.google.com/drive/folders/1GvhM2SwtNpjWqHrdry-2EFhJS3N_nFbT?usp=sharing)


