import os
import dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Load environment variables
dotenv.load_dotenv()

def main():
    # Load and split documents
    file_path = "./data/docs/pharmacydrugs.pdf"
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200, 
        add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    # Ensure the persist directory exists
    persist_dir = "./data/store/chroma_langchain_db"
    if os.path.exists(persist_dir):
        import shutil
        shutil.rmtree(persist_dir)
    os.makedirs(persist_dir, exist_ok=True)
    
    # Create vector store
    vector_store = Chroma(
        collection_name="pharmacydrugs_collection",
        embedding_function=embeddings,
        persist_directory=persist_dir,
        collection_metadata={"hnsw:space": "cosine"}
    )
    
    # Add documents
    try:
        ids = vector_store.add_documents(documents=all_splits)
        print(f"Successfully added {len(ids)} documents to the vector store")
        
        # Test the vector store
        results = vector_store.similarity_search("Describe ibuprofin")
        print("\nTest search result:")
        print(results[0].page_content[:200])
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 