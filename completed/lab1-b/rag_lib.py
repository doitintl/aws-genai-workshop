import os
from langchain.embeddings import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms.bedrock import Bedrock
from langchain.retrievers import AmazonKnowledgeBasesRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

def get_llm():
    
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": 0, 
        "topP": 0.5, 
        "stopSequences": [], 
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
        knowledge_base_id="<Knowledgebase id>",
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
    )
    
    return retriever

def get_rag_response(question): #rag client function
    
    llm = get_llm()
    retriever = get_retriever()
    
    qa = RetrievalQA.from_chain_type(
        llm=llm, retriever=retriever, return_source_documents=True
    )
    
    response = qa(question)
    
    formatted = response["result"]
    
    return formatted

