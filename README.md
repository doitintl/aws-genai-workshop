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

### Amazon Bedrock Setup

We will be using Amazon Bedrock  to access foundation models in this workshop.

Below we will configure model access in Amazon Bedrock in order to build and run generative AI applications. Amazon Bedrock provides a variety of foundation models from several providers.

1. Find Amazon Bedrock by searching in the AWS console.

![Bedrock search](./images/bedrock-search.png)

2. Expand the side menu.

![Bedrock side menu](./images/bedrock-menu-expand.png)

3. From the side menu, select Model access.

![Bedrock access link](./images/model-access-link.png)

4. Select the Manage model access button.

![Bedrock access](./images/model-access-view-subset.png)

5. Select the checkboxes listed below to activate the models. If running from your own account, there is no cost to activate the models - you only pay for what you use during the labs. Review the applicable EULAs as needed.

* AI21 > Jurassic-2 Ultra
* Amazon (select Amazon to automatically select all Amazon Titan models)
* Anthropic > Claude
* Cohere > Command
* Meta > Llama 2 Chat 13B
* Stability AI > SDXL 1.0

Click **Request model access** to activate the models in your account.

![Bedrock edit subset](./images/model-access-edit-subset.png)

6. Monitor the model access status. It may take a few minutes for the models to move from **In Progress** to **Access granted** status. You can use the Refresh button to periodically check for updates.

7. Verify that the model access status is **Access granted** for the previously selected models.

![Bedrock access](./images/model-access-complete-subset.png)

### AWS Cloud9 setup

We will be using AWS Cloud9  as our integrated development environment for this workshop. AWS Cloud9 is one option for building applications with Amazon Bedrock - you can also use your own development tools (VS Code, PyCharm, etc.), Amazon SageMaker Studio , or Jupyter Notebooks.

Below we will configure an AWS Cloud9 enviroment  in order to build and run generative AI applications. An environment is a web-based integrated development environment for editing code and running terminal commands.

**Assumptions for the following instructions**

* AWS Cloud9 will be run from the same account and region where Bedrock foundation models have been enabled.

* The acccount and region have a default VPC configured (this is the AWS default).

If you have any challenges below, you may need to access Bedrock from your desktop environment, or create an alte

1. In the AWS console, select the region that has Amazon Bedrock foundation models enabled.


2. In the AWS console, search for **Cloud9**
    * Select **Cloud9** from the search results

    ![search-cloud9](./images/search-cloud9.png)

3. Select **Create eenvironment**
    ![cloud9 welcome](./images/cloud9-welcome.png)

4. Set the environment details.
    * Set **Name** to bedrock-environment
    ![environment details](./images/environment-details.png)

5. Set the EC2 instance details
    * Set **Instance type** to **t3.medium**
    * Set **Platform** to **Ubuntu Server 22.04 LTS**
    * Set **Timeout** to 4 hours

    ![ubuntu instance](./images/cloud9-ubuntu-instance.png)

    **Did you select Ubuntu as your platform?**
Please double-check that you set Platform to Ubuntu Server 22.04 LTS. This ensures that you will have a Python version that can support LangChain and other critical libraries.


6. Select the **Create** button

    ![create button](./images/create-button.png)

7. Wait for the environment to be created.
    * You should get a "Successfully created bedrock-environment" message in the top banner when ready.
    * In the Environments list, click the Open link. This will launch the AWS Cloud9 IDE in a new tab.

    ![cloud9 ready](./images/cloud9-ready.png)

8. Confirm that the AWS Cloud9 environment loaded properly.
    * You can close the Welcome tab
    * You can drag tabs around to the position you want them in.
    
    ![cloud9 ide](./images/cloud9-ide.png)

### Lab setup

1. In the AWS Cloud9 IDE, select the bash termina

    ![cloud terminal](./images/cloud9-terminal.png)

2. Git clone repo

3. Install Requirements

        pip3 install -r requirements.txt

### Workshop

There are two folders in this repo:

* **completed**: This contains all labs with all the code ready to be run. The Readme will provide you insight into what the code is doing.

* **hands-on**: This contains the files required but without any code. The Readme will guide you on adding each code piece.

## Remember Have Fun!