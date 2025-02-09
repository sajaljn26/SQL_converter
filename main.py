import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

Groq_api_key = os.environ["GROQ_API_KEY"]

def get_sql_query_fom_text(user_query):
     groq_sys_prompt = ChatPromptTemplate.from_template("""
                    You are an expert in converting English questions to SQL query!
                    The SQL database has the name STUDENT and has the following columns - NAME, COURSE, 
                    SECTION and MARKS. For example, 
                    Example 1 - How many entries of records are present?, 
                        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
                    Example 2 - Tell me all the students studying in Data Science COURSE?, 
                        the SQL command will be something like this SELECT * FROM STUDENT 
                        where COURSE="Data Science"; 
                    also the sql code should not have ``` in beginning or end and sql word in output.
                    Now convert the following question in English to a valid SQL Query: {user_query}. 
                    No preamble, only valid SQL please
                                                       """)
     model="llama3-8b-8192"
     llm = ChatGroq(
     groq_api_key = os.environ.get("GROQ_API_KEY"),
     model_name=model
    )
   return sql_query
def main():
    st.set_page_config(page_title="Text to SQL")
    st.header("Talk to your database")
    
    user_query = st.text_input("Enter your query")
    submit = st.button("Submit")
    if submit:
        get_sql_query_fom_text
        st.header("Hi, I am your Assistant")

if __name__ == '__main__':
    main()