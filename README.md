### Learning to create embeddings and push to chromadb

##### Environment
- Platform: Mac Book Pro M1/16Gb ram
- OS: Mac OS Monterey 12.1
- Python: 3.10

##### Installation
```
$ pip install -U sentence-transformers
$ pip install chromadb
```
##### Files

1. `Chroma.ipynb` getting the basics for `Sentence Transformer`, creating embeddings and add it to `chromadb`. Mostly uses
examples from the websites - see references below

2. `process_news` pre-processes a text file containing news in a specific format and add the relevant records to `chromadb`

3.  Sample data as `.txt` files

4.  `util/text2json.py` functions to preprocess text file

5.  Otherfiles can be ignored.

   
##### References
(Sentences Transformers)[https://www.sbert.net/index.html]
(chromadb)[https://trychroma.com]

### NOTES for my reference
Source: LLM Practioners group

###### What are embeddings? 
[Great explainer](https://vickiboykis.com/what_are_embeddings/) by a an early practitioner trying to explain to herself and hence others. 

###### LLM-sbert 
15/Aug/2023
if you want to start at a lower level to see how embeddings ie vector encodings of sentences are computed and used see this - try typing into python interpreter command line - its very interesting to see the embedding vector of a small sentence.
https://www.sbert.net/docs/quickstart.html

###### Which LLM model to use?
(check out)[https://techcrunch.com/2023/08/17/arthur-releases-open-source-tool-to-help-companies-find-the-best-llm-for-a-job/]

###### App ollama!

For people on Macs I suggest the app called ollama - after install it operates on the command line and will allow you to pull models then run them. Will give you a prompt in the terminal. Small models that need 3-4G RAM work wonderfully well. You don’t need to do anything else or any other install. There is a discord channel called ollama for help but I’ve never needed any. Used it for summarizing text - works like a charm. They are creating a Linux version next.

###### SQL Lite for embeddings
Coauthor of Django framework Simon Williston works on SQLite3 for embeddings and in Jan 2023 stumbled upon RAG through his own independent exploration. 
How to implement Q&A against your documentation with GPT3, embeddings and Datasette
https://simonwillison.net/2023/Jan/13/semantic-search-answers/

###### PGVECTOR

###### RAG

- [Original RAG paper. ](https://arxiv.org/pdf/2005.11401.pdf)
- [Simplified explanation](https://medium.com/@amodwrites/understanding-retrieval-augmented-generation-a-simple-guide-d638ac92c123)