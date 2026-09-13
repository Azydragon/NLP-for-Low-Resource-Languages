vocab = ["ancient","complex","is","sanskrit"]
sent = ["ancient","is","ancient","sanskrit","is"]
vector=[0]*len(vocab)
for word in sent:
  if word in vocab:
    position=vocab.index(word)
    vector[position]+=1
print(vector)
