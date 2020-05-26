
## How to get started
Steps-
1. Create new folder named `bin` in root path
1. Download [`stat.split.pickle`](https://github.com/ysenarath/sinling/releases/download/v0.1-alpha/stat.split.pickle) to the `bin` folder
1. Import required tools from the `sinling` module in your desired project 
(you may have to append this project path to your path environment variable)

## How to use
### Sinhala Tokenizer
```python
from sinling import SinhalaTokenizer

tokenizer = SinhalaTokenizer()

sentence = '...'  # your sentence

tokenizer.tokenize(sentence)
```

Sinhala tokenizer also includes `tokenizer.split_sentences(...)` function for splitting sentences.

### Word Joiner (Morphological Joiner)
```python
from sinling import preprocess, word_joiner

w1 = preprocess('මුනි')
w2 = preprocess('උතුමා')
results = word_joiner.join(w1, w2)
# Returns a list of possible results after applying join rules ['මුනිතුමා', ...]
```

### Word Splitter (Morphological Splitter) / corpus based - *experimental*
```python
from sinling import word_splitter

word = '...'
results = word_splitter.split(word)
# Returns a dict containing debug information, base word and affix
```

## Special Notice
This project is still in work in progress status. Use at Your Own Risk.
