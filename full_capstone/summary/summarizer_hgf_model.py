from transformers import AutoModelWithLMHead, AutoTokenizer, AutoModelForSeq2SeqLM
from nltk import sent_tokenize
from aylienapiclient import textapi

tokenizer_hgf = AutoTokenizer.from_pretrained('./summary/models/hgf_model')
model_hgf = AutoModelForSeq2SeqLM.from_pretrained('./summary/models/hgf_model')

def split_group(sentences, cap = 600):
  """split the long documents to fit the HuggingFace tokens limit

  Args:
      sentences (str): text
      cap (int, optional): the limit length for each subset. Defaults to 600.

  Returns:
      (list) the lists of splitted sentences to fit into HGF
  """  
  if type(sentences) == str:
    sentences = sent_tokenize(sentences)
    
  split = [[]]
  cur_val = 0

  # check if the tokens exceed the limit, then pass it to the next batch
  for sen in sentences:
    val = len(sen.split(" "))
    if cur_val + val <= cap:
      split[-1].append(sen)
      cur_val += val
    else:
      cur_val = 0
      split.append([])
      split[-1].append(sen)
      cur_val += val
  return split

def summarize_hgf(txt):
  """summarize using HGF model

  Args:
      txt (str): text 

  Returns:
      (str) summary
  """  
  inputs = tokenizer_hgf.encode(txt, return_tensors="pt")
  outputs = model_hgf.generate(inputs)
  result = tokenizer_hgf.decode(outputs[0])
  return result[7:-4]

def summarizer_hgf_get(text, percent_sentences = 50):
  """get the hgf summarization after splitting the sentences and fit into the transformer model

  Args:
      text (str): the text to summarize
      percent_sentences (int, optional): percent to retain. Defaults to 50.

  Returns:
      dictionary with the method [method], summary [sentences], number of sentences [summary_num_sentences]
  """    
  
  num_sentences = int(percent_sentences / 100 * len(sent_tokenize(text)))
  
  # if fail, use aylien
  try:

    # split sentences to fit the token limit
    summary = ""
    split_texts = split_group(text)
    for item in split_texts:
      current_text = "".join(item)
      current_summary = summarize_hgf(current_text)
      summary += current_summary + " "
    
    sentences = sent_tokenize(summary)
    
    # summarize each batch and append the results
    # output
    output = {'sentences': summary, 'summary_num_sentences': len(sentences), "method": "hgf"}
    print("HGF works!")
    return output

  # use aylien if failed
  except:
    output = {}

    # send requests to aylien
    client = textapi.Client("79e389d3", "1bc2400da0cb4745c30fb68b67e5e5cf")

    out = client.Summarize({'sentences_number': num_sentences,
                            'text': text,
                            'title': "Class reading"})

    output['summary_num_sentences'] = num_sentences
    output['sentences'] = "".join([" " + val for val in out['sentences']])[1:]
    output['method'] = "aylien"
    print("Bert transformer failed! Use aylien")
    return output
