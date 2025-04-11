import os
from typing import List, Dict
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
from knowledge_base import get_knowledge_base_data


class RAGAgent:
    """Customer Support Agent using RAG with Memory (Session-Based)."""

    def __init__(self, api_key: str):
        # Configure generative AI
        genai.configure(api_key=api_key)
        self.embedding_model = "models/text-embedding-004"
        self.generation_model = genai.GenerativeModel("gemini-2.0-flash")

        # Create a ChromaDB client instance
        self.chroma_client = chromadb.PersistentClient(path="chroma_db")

        # Load knowledge base data
        self.products, self.policies = get_knowledge_base_data()

        # Initialize or retrieve knowledge base collection
        self.collection = self._initialize_knowledge_base()

        # **Initialize memory** (session-based)
        self.memory: List[Dict[str, str]] = []

    def _initialize_knowledge_base(self) -> chromadb.Collection:
        """Initialize or retrieve the Chroma collection."""
        collection = self.chroma_client.get_or_create_collection(
            name="knowledge_base",
            embedding_function=embedding_functions.GoogleGenerativeAiEmbeddingFunction(
                api_key=os.getenv("GEMINI_API_KEY"),
                model_name=self.embedding_model,
            ),
        )

        # Check if knowledge base exists
        existing_docs = 0
        try:
            results = collection.query(query_texts=["init_check"], n_results=1)
            existing_docs = len(results["ids"][0])
        except Exception:
            pass

        # Populate knowledge base if empty
        if existing_docs == 0:
            documents, metadatas, ids = [], [], []

            # Product data
            for idx, product in enumerate(self.products):
                doc_text = (
                    f"Product Information:\n"
                    f"Name: {product['name']}\n"
                    f"Price: {product['price']}\n"
                    f"Features: {product['features']}\n"
                    f"Colors: {product['colors']}\n"
                    f"Availability: {product['availability']}\n"
                    f"Warranty: {product.get('warranty', 'N/A')}"
                )
                documents.append(doc_text)
                metadatas.append({"type": "product", "product_name": product["name"]})
                ids.append(f"product_{idx}")

            # Policy data
            for idx, policy in enumerate(self.policies):
                doc_text = f"Policy Information:\nType: {policy['type']}\nDetails: {policy['content']}"
                documents.append(doc_text)
                metadatas.append({"type": "policy", "policy_type": policy["type"]})
                ids.append(f"policy_{idx}")

            collection.add(documents=documents, metadatas=metadatas, ids=ids)

        return collection

    def retrieve_context(self, query: str, top_k: int = 4) -> List[str]:
        """Retrieve relevant context for the query."""
        results = self.collection.query(query_texts=[query], n_results=top_k)
        return results.get("documents", [[]])[0]

    def generate_response(self, query: str, context: List[str]) -> str:
        """Generate response using Gemini and memory."""
        # Combine conversation history with the new query
        memory_context = "\n".join(
            [f"User: {m['query']}\nAgent: {m['response']}" for m in self.memory[-5:]])  # Keep last 5 exchanges

        # Construct prompt with memory
        prompt = (
            "You are a helpful customer support agent. Answer the user's question "
            "using the provided context. Analyze if this is a question about products or policies "
            "and respond accordingly. Follow these guidelines:\n"
            "1. Respond in complete, flowing paragraphs using natural language.\n"
            "2. Include ALL relevant details from the context in your answer.\n"
            "3. Avoid bullet points, lists, or markdown formatting.\n"
            "4. Mention numbers and specifications explicitly.\n"
            "5. For policies, explain all key points in full sentences.\n"
            "6. For products, explain all key points in full sentences.\n"
            "7. Maintain a friendly and professional tone.\n"
            "8. Use past conversation history to provide relevant and coherent responses.\n"
            "9. Do not repeat details the user has already been informed about when asked about a follow question.\n"
            

            "Conversation History:\n"
            f"{memory_context}\n\n"

            "Context:\n"
            f"{'\n\n'.join(context)}\n\n"

            f"User Question: {query}\n"
            "Answer:"
        )

        try:
            response = self.generation_model.generate_content(prompt).text.strip()
            # Store in memory
            self.memory.append({"query": query, "response": response})
            return response
        except Exception:
            return "I encountered an error generating a response. Please try again."

    def reset_memory(self):
        """Clear conversation memory."""
        self.memory = []
