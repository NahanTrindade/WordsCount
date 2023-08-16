from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
words=[]

def chave(e):
    return e['ocorrencia']

for line in sys.stdin:
    line = line.strip()
    line=line.lower()

    word, count = line.split('\t', 1)
    try:
      count = int(count)
    except ValueError:
      continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            words.append({'palavra':current_word, 'ocorrencia':current_count})
        current_count = count
        current_word = word
if current_word == word:
    words.append({'palavra':current_word, 'ocorrencia':current_count})

print('Palavras distintas:', len(words))
print('\n')
words.sort(reverse=True,key=chave)
print('As 10 palavras que mais ocorrem:')
for i in range(10):
  print(words[i]['palavra'])
print('\n')
print('Histograma:')
for i in range(10):
  print(words[i]['palavra'],' ',words[i]['ocorrencia'])




