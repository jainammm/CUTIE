'''
Create Vocab From traning image texts
'''

import json
import os

directory = 'Images'

texts = ''

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = directory + '/' + filename

        with open(file_path) as json_file:
            data = json.load(json_file)

        for text in data['text_boxes']:
            texts += ' ' + text['text']

corpus_file = 'corpus.txt'

with open(corpus_file, 'w') as fout:
    fout.write(texts)

from tokenizers import BertWordPieceTokenizer

# Initialize an empty BERT tokenizer
tokenizer = BertWordPieceTokenizer(
  clean_text=False,
  handle_chinese_chars=False,
  strip_accents=False,
  lowercase=True,
)

# prepare text files to train vocab on them
files = [corpus_file]

# train BERT tokenizer
tokenizer.train(
  files,
  vocab_size=500,
  min_frequency=1,
  show_progress=True,
  special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
  limit_alphabet=1000,
  wordpieces_prefix="##"
)

# save the vocab
# tokenizer.save('vocab.txt', True)
vocab = json.loads(tokenizer.to_str(True))

with open('vocab.txt', 'w') as fout:
    for token in vocab['model']['vocab']:
        fout.write(token + '\n')
        