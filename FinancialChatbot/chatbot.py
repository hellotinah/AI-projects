from flask import Flask, request, render_template, jsonify
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
import faiss
import numpy as np

app = Flask(__name__)

# Load the document
loader = TextLoader("./complete_financial_analysis.txt")
docs = loader.load()

# Extract text from the Document object
text = docs[0].page_content  # Assuming there's only one document loaded

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

# Split the text into chunks
texts = text_splitter.create_documents([text])

# Initialize OpenAI embeddings
embeddings_model = OpenAIEmbeddings(openai_api_key="your_openai_key")

# Create embeddings for the text chunks
chunk_texts = [doc.page_content for doc in texts]  # Extract text from the Document objects
embeddings = embeddings_model.embed_documents(chunk_texts)

# Convert embeddings to numpy array
dimension = len(embeddings[0])
vectors = np.array(embeddings).astype('float32')

# Create and populate FAISS index
index = faiss.IndexFlatL2(dimension)
index.add(vectors)

# Create retriever function
def retrieve(query_text, k=5):
    query_vector = np.array(embeddings_model.embed_query(query_text)).reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    return distances, indices

# Initialize HuggingFace LLM
huggingface_api_token = "your_huggingface_openai_token"  # Replace with your actual HuggingFace API token
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    top_k=30,
    temperature=0.1,
    max_new_tokens=512,
    repetition_penalty=1.03,
    huggingfacehub_api_token=huggingface_api_token
)

# Define the prompt template
template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
prompt = ChatPromptTemplate.from_template(template)

# Define your Flask routes
@app.route('/')
def home():
    return render_template('bot_1.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_input']
    
    # Retrieve relevant documents
    distances, indices = retrieve(user_message)
    
    # Get the retrieved documents based on indices
    retrieved_texts = [texts[idx].page_content for idx in indices[0] if idx < len(texts)]
    
    # Prepare context for the LLM
    context = "\n\n".join(retrieved_texts)
    prompt_text = prompt.format(context=context, question=user_message)
    
    # Generate response using LLM
    response = llm(prompt_text)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
