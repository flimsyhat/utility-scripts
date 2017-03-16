import re
from markov_playback import build_markov_chain, build_output

txt = open("animal_behavior.txt")

words = []

regex = re.compile('([,.!?"])')

for line in txt:
    new_line = regex.sub(r' \1 ', line)
    for word in new_line.split():
	words.append(word.lower())

chain = build_markov_chain(words)
print build_output(chain, 1000, "synanthropes")
