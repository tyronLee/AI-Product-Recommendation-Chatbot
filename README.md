# AI Product Recommendation Chatbot using Google Sheets
This is an AI sales assistant RAG application that links to a Google Sheets spreadsheet containing a list of Products and their prices. This data was web-scraped from amazon.co.za using Power Automate Desktop. The spreadsheet file is also attached. The AI assistant takes a user's question about products in the spreadsheet and makes recommendations based on that question. 

This particular version of the application uses Llama3.1 as the LLM and nomic-embed-text as the embedding model. Both models are running locally on my computer using Ollama and the response time for all questions tested is less than 5 seconds if the model is already in memory. ChromaDB is the vector database used. Other models, like OpenAI's GPT-4o, can also be used by changing one or two lines of code.

## Demo
Some sample responses given by the AI assistant are shown below:
<br>
<br>

![Screenshot 2025-03-03 155455](https://github.com/user-attachments/assets/871f836e-1b6b-4a7a-820e-ffd55a5150f6)
The user is asking for a laptop recommendation based on the brand name. The application goes even further by recommending additional items like a backpack.
<br>
<br>
<br>


![Screenshot 2025-03-03 155851](https://github.com/user-attachments/assets/98792703-170d-47a5-bbb7-684c4060815e)
The user is asking for a laptop recommendation based on the brand and what the laptop would be used for.

<br>
<br>
<br>

![Screenshot 2025-03-03 155955](https://github.com/user-attachments/assets/8b630bc2-3229-4f47-ae71-f0d7bfb8a6c1)
User asking for a laptop recommendation based on their budget. The system goes further by recommending other products outside of this price range and the benefits that come with the more expensive versions.

<br>
<be>

## Future Work
As you can see from the products spreadsheet, I also scraped some image links for each product. The goal is to display an image next to each recommended product. The application can also be easily run as an API and integrated into already existing web applications.
