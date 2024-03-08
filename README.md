# Gen AI Workshop with DoiT International

This workshop is aimed to give you an introduction hands-on experience with Bedrock, Langchain, and Streamlit.

* **Bedrock** - Fully mnanage service that offers high-performing foundational models from leading AI companies such as AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a single API.

    * **Knowledgebase**: Managed document retrieval service for RAG architecture. The service leverages OpenSearch Servelerss or Aurora Postgress Serverless with embedding models to deliver a robust solution.

    * **Agents**: Managed service to integrate GenAI workflows with any other system to enhance the experience by allowing custom actions based on specific situations.

    * **Model Evaluation**: Evaluate models againsta a specific set of prompts or a custom prompt dataset. This allows to continously understand the quality of the models againsts specific knoeledge domains.

<br>

* **langchain** - Is a framework for developing applications powered by language models. It enables applications that:

    * **Are context-aware**: connect a language model to sources of context (prompt instructions, few shot examples, content to ground its response in, etc.)
    * **Reason**: rely on a language model to reason (about how to answer based on provided context, what actions to take, etc.)

<br>

* **streamlit** - Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

## Getting started

If you are using AWS Cloud9 you can skip this and go to the next sension.

### Install Requirements

        conda create -n "bedrock-workshop" python=3.10
        conda activate bedrock-workshop
        pip install -r requirements.txt


### Workshop

There are two folders in this repo:

* **completed**: This contains all labs with all the code ready to be run. The Readme will provide you insight into what the code is doing.

* **hands-on**: This contains the files required but without any code. The Readme will guide you on adding each code piece.

## Remember Have Fun!