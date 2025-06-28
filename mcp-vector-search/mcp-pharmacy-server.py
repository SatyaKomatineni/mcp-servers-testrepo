from fastmcp import FastMCP
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("Pharmacy Context Server")

database = "./data/store/chroma_langchain_db"

# Initialize embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

#
# Initialize ChromaDB
vector_store = Chroma(
    collection_name="pharmacydrugs_collection",
    embedding_function=embeddings,
    persist_directory="./data/store/chroma_langchain_db", 
)

@mcp.tool(name="pharmacy_drug_search", description="Search for pharmacy drugs in the vector database for relevant documents and return aggregated results.")
def pharmacy_drug_search(pharmcy_drug_search_query: str, separator: str = "\n\n") -> str:
    """
    Search for pharmacy drugs in the vector database for relevant documents and return aggregated results.
    
    Args:
        pharmcy_drug_search_query: The pharmacy drug search query string
        separator: String to use between aggregated results (default: "\n\n")
    
    Returns:
        Aggregated text results from the pharmacy drug search
    """
    # Perform similarity search
    docs = vector_store.similarity_search(pharmcy_drug_search_query)
    
    # Extract and aggregate text content
    results = [doc.page_content for doc in docs]
    return separator.join(results)

if __name__ == "__main__":
  mcp.run(transport="streamable-http", host="127.0.0.1", port=9002)