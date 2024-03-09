import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationalRetrievalChain

from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.retrievers import AmazonKnowledgeBasesRetriever


def get_llm():
        
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": ["Human:"], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #set the foundation model
        model_kwargs=model_kwargs) #configure the properties for Claude
    
    return llm


def get_retriever():
    retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id="5GKRWWX1V9",
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
    )
    
    return retriever


def get_memory(): #create memory for this chat session
    
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True) #Maintains a history of previous messages
    
    return memory


def get_rag_chat_response(input_text, memory): #chat client function
    
    llm = get_llm()

    retriever = get_retriever()
    
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)
    
    chat_response = conversation_with_retrieval({"question": input_text}) #pass the user message and summary to the model
    
    return chat_response['answer']
