from flask import Flask, render_template, request
import numpy as np

# Sample Corpus (Replace with your actual corpus)
corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Convert corpus to vectors (Simplified example, use a proper embedding model)
def vectorize_text(text):
    # This is a simplified example. Use a proper embedding model (e.g., Word2Vec, GloVe)
    words = text.lower().split()
    vector = np.random.rand(10)  # Replace with actual embedding vectors
    return vector

corpus_vectors = [vectorize_text(doc) for doc in corpus]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        query_vector = vectorize_text(query)

        # Calculate dot product similarities
        similarities = [np.dot(query_vector, doc_vector) for doc_vector in corpus_vectors]

        # Get indices of top 10 most similar documents
        top_10_indices = np.argsort(similarities)[::-1][:10]

        # Retrieve top 10 most similar documents
        top_10_results = [corpus[i] for i in top_10_indices]

        return render_template('results.html', results=top_10_results)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)