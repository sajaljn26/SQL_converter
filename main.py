import streamlit as st
import sqlite3
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

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
    
    model = "llama3-8b-8192"
    llm = ChatGroq(
        groq_api_key=Groq_api_key,
        model_name=model
    )
    
    
    chain = groq_sys_prompt | llm | StrOutputParser()
    sql_query = chain.invoke({"user_query": user_query})
    return sql_query
def get_data_from_database(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()



def main():
    st.set_page_config(page_title="Text to SQL")
    st.header("Talk to your database")
    
    user_query = st.text_input("Enter your query")
    submit = st.button("Submit")
    
    if submit:
        sql_query = get_sql_query_fom_text(user_query)
        retrieve_data = get_data_from_database(sql_query)
        st.header(f"Retrieving data from the Database with the Query: [{sql_query}]")
        for row in retrieve_data:
            st.header(row)

if __name__ == '__main__':
    main()
