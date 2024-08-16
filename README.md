# Workbooks AI Application

Bubble is a full-stack, no-code app builder. You can build scalable applications with this AI-powered no-code development platform. You can also connect your app with ChatGPT or Claude. If you love reading like I do, you may come across countless workbooks. To make sure you ace them, you can stay organized and have them all in one place. Bubble can help you with that by gathering the workbooks listed in your favorite book in one place. This application is powered by the OpenAI API, and everything is done via the UI. Here are the steps to make one for you:

### Step 1: Set the API Connector

#### 1. Install the API Connector
   
![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(2).png?raw=true)
   
#### 2- Connect it to OpenAI by filling in the headers as follows:

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(3).png?raw=true)
    
Make sure to replace `Bearer "YOUR_OPENAI_KEY_KEY"` with your actual OpenAI key. In this particular project, we used one API call, and that is to the Chat Completions Model. It is a POST request, and we are making a POST request to the following URL:         
`https://api.openai.com/v1/chat/completions`. You can change the `max_tokens` variable to make the application more scalable.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(4).png?raw=true)
    
Then click on Reinitialize Call and make sure that the messade_content's type is text.
    
#### 3- Create a new data type:

To store the files that are related to each user, you need to create a new data type.
Navigate through the Data Types and create a new data type called PDFs.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(11).png?raw=true)
    
In the PDFs data type, create the following fields: `PDF` of type `file`, `content` of type `text`, `Full name` of type `text`

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(12).png?raw=true)
    
#### 4- Create the Sign-up page:

Because we are using the users data, we need to create the sign-up page to get data from users.
Create a New Page, thne click on Components, then choose the Sign-up Page and drag it into the new page.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(13).png?raw=true)

Feel free to be creative with the UI design.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(1).png?raw=true)

Click on `Workflow` tab, then `Add a new event` then choose the event "When page is loaded"
Click on the event to add a new action, choose `ElementActions` and then `Toggle` and select `Popup Sign Up/Log in` as the element to be toggled when the page loads.
Click on the Sign up bntton and click Add Workflow, then click on Add an action -> Account -> Sign the user Up 

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(14).png?raw=true)

Fill in the fields as shown below:

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(15).png?raw=true)

The next step of the workflow is to naviagte the user to another page, create a new page in the Design section and then add another action to the workflow, by taping Workflows -> Navigation -> Go to another Page

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(16).png?raw=true)
    
#### 5- Upload PDFs page:

Go to the design section of your new page, and drag the File Uploader element onto the page. You can place it wherever you think it looks best.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(10).png?raw=true)

Navigate to the Workflow section, click on Add an event, select Elements -> an input’s value is changed.
Add an action -> Data -> Create a new thing, set the Type variable to PDFs and then set another field as PDF = This FileUploader’s value.
Add another action -> Data -> Make changes to things and fill in the fields as needed:

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(18).png?raw=true)
    
#### 6- Convert PDF to Text:

Install the Convert PDF to Text Plugin:
Go to your workflow and add a new action -> Select Plugins -> Convert PDF to Text -> Set the pdf-url to ThisFileUploader's value.
Add another action -> Data -> Make changes to a thing and you fill with the following

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(19).png?raw=true)

This action will add the PDF text to the content field of the PDF.
When sending data to the OpenAI API, consider the number of tokens to reduce cost, you can summarize the PDF text:
Go to Data -> PDFs -> Data Types -> Create a new field called summary and set the type to text.
Add an Action to Summarize the Text Using OpenAI -> Select Plugins -> Choose OpenAI - GPT (ensure the OpenAI and ChatGPT plugin is installed) and Fill in the fields as shown in the image below:

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(20).png?raw=true)

#### 7- ChatGPT plugin

Now you can interact with the PDF content and ask questions. But first, let's clean up the UI so that the user can upload multiple PDFs.
First, reset inputs by create another action, then select Elements actions -> Choose Reset inputs.

We can also show a Message When a PDF is Successfully Uploaded:
Go to the Design section -> Drag the Browser plugin into the page (make sure it is already installed) -> Go back to the Workflows section -> Add another action -> Select Element Actions -> Choose Show alert Pop up in Browser -> Write the message you want to display.
    
Now, feed the Knowledge Base to OpenAI:
Add another action -> Select Plugins -> Choose OpenAI - GPT (make sure the OpenAI and ChatGPT plugin is installed) -> Fill in the fields as follows:

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(21).png?raw=true)

#### 8- Display the result

To display the result in the page:
First, go to the Design section -> Add a Text element to the page -> Click outside the page -> Click the "i" icon -> Create a new custom state, call it "result", and set the type to text.

Next, we need to set the Text Element:
Click on the Text element -> In the appearance section, set it to page_name's result.

Finally, set the State in the Workflow Section:

Go to the Workflow section -> Add another action -> Select Element Actions -> Choose Set State and fill in the fields as shown below (replace "storepdfs" with your actual page name):

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/WorkbookAI/Screenshot%20(22).png?raw=true)

You can be creative and add an input section to ask questions about the workbooks and get answers as well.

# Travel AI Application

This project involves building an AI travel agent that helps you plan your travels based on your preferences.

## Make: Automation Software

Make is a no-code platform that allows you to visualize, create, build, and automate workflows.
This Make scenario is designed to generate a custom travel plan based on a user's interests and then store the generated plan in a Notion database. It connects to OpenAI's GPT-3 and Notion to achieve this. The Basic Repeater ensures the actions are repeated a specified number of times, the OpenAI GPT-3 module generates the travel plan, and the Notion module stores the plan in a database.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/TravelBot/Screenshot%20(7).png?raw=true)

#### Basic Repeater (Module ID: 8)

This module repeats a set of actions a specified number of times. It will repeat the subsequent actions three times, starting from 1 and incrementing by 1 each time.
* Configuration:
    - Start: 1
    - Repeats: 3
    - Step: 1

#### Transform Text to Structured Data (OpenAI GPT-3) (Module ID: 1)

This module uses OpenAI's GPT-3 to transform a text prompt into structured data. It generates a custom travel plan based on the user's interests in specific anime and outputs structured data.
* Configuration:
    - Model: gpt-4o
    - Prompt: "You are a personal travel agent with the goal of designing a custom travel plan from west coast Vancouver to the east coast North America. I’ve been really into anime like Frieren, kino's journey, and Somali and the forest spirit so I’d like to replicate some of their travels but on earth. Suggest a detailed plan for me. Eg: Title, date, location, nearest city/country, description, number of hours, category, weather."
    - Raw Text: {{executionId}}
    - Parameters:
        - Title (Type -> Title)
        - Date (Type -> Text)
        - Location (Type -> Text)
        - City (Type -> Text)
        - Description (Type -> Text)
        - Hours (Type -> Number)
        - Category (Type -> Text)
        - Weather (Type -> Text)
          
    Make sure to use a valid OpenAI Key.
  
#### Create a Page (Notion) (Module ID: 2)

This module creates a new page in a specified Notion database using the structured data generated by the previous module. It creates a new page in the specified Notion database with the travel plan details.
* Configuration:
    - Database ID: "your_data_base_id"
    - Fields Mapping:
        - Title: `{{1.Title}}`
        - Category: `{{1.Category}}`
        - Location: `{{1.Location}}`
        - Hours: `{{1.Hours}}`
        -Description: `{{1.Description}}`
        - Date: `{{1.Date}}`
        - Weather: `{{1.Weather}}`
        - City: `{{1.City}}`
    Make sure you create a database in notion with the same columns names and data types.
    To find the database ID, navigate to the Notion page where your database is locate, then Click on the database to open it, look at the URL in your browser's address bar. It will look something like this:
    `https://www.notion.so/yourworkspace/Database-Name-6feda45bc86e424488b4e534f63ee923`
    The Database ID is the long string of characters after the last slash (/) in the URL. In the example above, the Database ID is:
    `6feda45bc86e424488b4e534f63ee923`.

![Alt text](https://github.com/KaoutharBousbaa1/AIProjects/blob/main/TravelBot/Screenshot%20(8).png?raw=true)

## Streamlit Dashboard

This part of the project sends an API request to OpenAI's model to generate travel suggestions, which are then saved as a CSV file named `itinerary_events.csv`. Next, it generates a Streamlit dashboard, and the Python script also creates a Google Map with the locations suggested by the AI.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/TravelBot/Screenshot%20(11).png?raw=true)

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/TravelBot/Screenshot%20(10).png?raw=true)

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/TravelBot/Screenshot%20(12).png?raw=true)

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/TravelBot/Screenshot%20(9).png?raw=true)

To run the project:

* Open the terminal and navigate to the project folder.
* Run the following commands:
    ```sh
    pip install --upgrade pip
    ```
    ```sh
    pip install -r requirements.txt
    ```
* Open `streamlit.ipynb` and run it in your IDE.
* Run the following scripts in the terminal:
    ```sh
    python generate_coordinates.py
    ```
    ```sh
    streamlit run streamlit_app.py
    ```

Make sure to use a valid OpenAI key and enable the Geocoding API in your Google Cloud Account, and ensure you use a valid API key.

# AI Music Generator

The project involves creating music playlists using AI tools. It starts with generating multiple songs on the Udio platform. A script is written to connect the individual songs into a cohesive playlist, which is outputted in MP3 format. Text lyrics, potentially obtained through Whisper-1, are then transformed into prompts that encapsulate the imagery, mood, and vibes of the songs. These prompts are fed into DALL·E to generate corresponding images. Finally, the project combines the playlist with the generated images to create an MP4 file, resulting in a visually beautiful music experience.

To run the project:

* Generate AI music via the Udio platform. You can sign up [here](https://www.udio.com/).
* Open the terminal and navigate to the project folder.
* Download FFmpeg from [here](https://github.com/BtbN/FFmpeg-Builds/releases/).
* Add the bin directory inside the extracted FFmpeg folder to your system's PATH environment variable.
* Run the following commands:
     ```sh
    pip install -r requirements.txt
    ```
    ```sh
    python playlist.py
    ```
    ```sh
    python playlist_images.py
    ```

Make sure to use a valid OpenAI key.

# Personal Finance Chatbot

This project aims to create a personal finance chatbot that helps you understand your spending habits and achieve financial goals. The chatbot, designed with the positive and perceptive personality of Might Guy from Naruto, uses GPT4All for prompt engineering and operates locally to ensure privacy. Users can interact with the chatbot using their CSV financial statements to analyze current spending habits. The project involves enhancing the chatbot's capabilities with Ollama in a Jupyter Notebook to categorize transactions and generate visualizations using a Plotly dashboard.

![Alt text](https://github.com/hellotinah/AI-Projects/blob/main/FinancialChatbot/Screenshot%20(1).png?raw=true)

Advanced features include integrating Retrieval-Augmented Generation (RAG) with LangChain and Flask, allowing the chatbot to provide more accurate and reliable financial advice through a lightweight web application. This comprehensive approach combines local execution, data privacy, and advanced AI techniques to offer insightful and actionable financial guidance.

To run the project:

* Download and install Ollama [here](https://ollama.ai/).
* Open the terminal, navigate to the project and run the following commands:
    ```sh
    ollama pull ollama2
    ```
    ```sh
    pip install --upgrade pip
    ```
    ```sh
    pip install -r requirements.txt
    ```
* Run the Jupyter notebook in your IDE: `categorize_expenses.ipynb` to categorize your expenses.
* Run the Jupyter notebook in your IDE: `dashboard.ipynb` to generate the dashboard.
* Run the application by using the command:
    ```sh
    python chatbot.py
    ```

Make sure to use a valid OpenAI key and a valid Huggingface API key.
# AI-projects
