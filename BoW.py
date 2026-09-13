import re

# 1. Our corpus of raw text sentences
corpus = [
    "Sanskrit is ancient and precise.",
    "Python is precise and simple.",
    "Ancient grammar is simple."
]

# Helper function to clean and tokenize a sentence
def tokenize(text):
    text = text.lower()
    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text.split()

# Tokenize all sentences into a list of token lists
all_token_lists = [tokenize(doc) for doc in corpus]

# -------------------------------------------------------------
# TODO STEP 1: Build a sorted list of unique vocabulary words
# Hint: Combine all tokens into a single set, then use sorted()
# -------------------------------------------------------------
all_tokens_flat = [token for token_list in all_token_lists for token in token_list]

vocab = sorted(list(set(all_tokens_flat))) # YOUR CODE HERE (Hint: convert set to sorted list)

print("Vocabulary:", vocab)
print("Vocab Length:", len(vocab))

# -------------------------------------------------------------
# TODO STEP 2: Write a function to turn tokens into a BoW vector
# -------------------------------------------------------------
def create_bow_vector(doc_tokens, vocabulary):
    # Create a list of zeros matching the size of vocabulary
    vector = [0] * len(vocabulary)

    # Loop over each token in the document
    for word in doc_tokens:
        if word in vocabulary:
            # Find the index of the word in vocabulary and increment vector
            index = vocabulary.index(word) # YOUR CODE HERE
            vector[index] += 1             # YOUR CODE HERE

    return vector

# Let's test your code on Document 1: "Sanskrit is ancient and precise."
doc1_tokens = all_token_lists[0]
doc1_vector = create_bow_vector(doc1_tokens, vocab)

print("\nDocument 1 Tokens:", doc1_tokens)
print("Document 1 Vector:", doc1_vector)
