import pandas as pd
from google.oauth2.service_account import Credentials
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
import gspread
import ollama

CREDENTIALS_FILE = "{Insert_Credentials_JSON_File_From_Google}"

def fetch_data_from_sheets():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("{Insert_Credentials_JSON_File_From_Google}", scopes=scopes)
    client = gspread.authorize(creds)
    sheet_id = "{Insert_Spreadsheet_ID}"
    sheet = client.open_by_key(sheet_id)
    
    data = sheet.sheet1.get_all_records()
    return pd.DataFrame(data)

def index_data(df):
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    
    db = Chroma(persist_directory="./db/chromadb", embedding_function=embedding_model)
    
    docs = [
        Document(
            page_content=row["Product"],
            metadata={
                "Price": row["Price"],
                "Image": row["Image"]
            }
        )
        for _, row in df.iterrows()
    ]
    
    db.add_documents(docs)
    print("Data indexed successfully!")

def main():
    index_data(fetch_data_from_sheets())

if __name__ == "__main__":
    main()
