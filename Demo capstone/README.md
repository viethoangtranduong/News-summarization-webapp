# Demo capstone

## The demo results folder

The file structure for this ```Demo capstone```:

- ```Crawling```: The folder contains all the functions related to crawling websites for content.
    - ```Crawling all.ipynb```: The notebook contains all the codes for crawling. All the functions are written in full.
    - ```Crawling demo.ipynb```: The notebook contains the demo of the crawling functions. The functions are imported from the .py files in the ```get_content``` folder.
- ```Summarization```: The folder contains all the functions related to summarization methods.
    - ```Summarization all.ipynb```: The notebook contains all the codes for summarization. All the functions are written in full.
    - ```Summarization demo.ipynb```: The notebook contains the demo of the summarization functions. The functions are imported from the .py files in the ```summary``` folder.
    - ```[Test] Create summarization.ipynb```: The notebook contains the code for summarizing the test data (test data retrieve from [Cornell newsroom dataset](https://lil.nlp.cornell.edu/newsroom/index.html)). The summaries are stored in the ```summarized.csv``` file.
    - ```[Test] Visualize ROUGE score.ipynb```: The notebook to visualize the ROUGE score performance of the models, including histograms and half-violin plots, with the 95% confidence interval.
    - ```summarized.csv```: summaries output of the test data.
- ```Visualization``: The folder contains all the functions related to visuailizing the content.
    - ```Visualization all.ipynb```: The notebook contains all the codes for visualization. All the functions are written in full.
    - ```Visualization demo.ipynb```: The notebook contains the demo of the visualization functions. The functions are imported from the .py files in the ```get_viz``` folder. 
    - The images are the output of the ```Visualization demo.ipynb``.



## Steps to run the code

Move the local directory to the current full_capstone folder

### Step 1: virtual environment
#### 1.1. Create virtual environment:
```
virtualenv capstone_venv
```

#### 1.2. Activate virtual environment
On Windows: 
```
capstone_venv\Scripts\activate
```
On Linux/Ubuntu:
```
capstone_venv/bin/activate
```

### Step 2: Install dependencies
```
pip install -r requirements.txt
```
(or pip3, depending on your default pip version)

For Pytorch, follow the instructions here to make it most compatible with your device: https://pytorch.org/get-started/locally/

### Step 3: Unzip the embeddings
Unzip the embeddings file at ```full_capstone/summary/vectorization/glove.6B.50d.zip``` and store the ```glove.6B.50d.txt``` file under ```full_capstone/summary/vectorization/glove.6B.50d.txt```

### Step 4: Run web app:
```
python application.py
```
(or python3, depending on your default python)


### Step 5: Interact with web app:
The web app should be ready at ```http://127.0.0.1:5000/``` or ```localhost:5000```
