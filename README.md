# Text-to-SQL Converter

A Streamlit application that converts natural language questions to SQL queries using Groq LLM API. Perfect for querying student databases without SQL knowledge.

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   pip install streamlit langchain-groq python-dotenv
   ```

2. Create `.env` file with your API key:
   ```bash
   GROQ_API_KEY=your_key_here
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 💾 Database Schema

The application works with a STUDENT database containing:
- NAME
- COURSE
- SECTION
- MARKS

## 📝 Example Queries

- "How many total students are there?"
  ```sql
  SELECT COUNT(*) FROM STUDENT;
  ```

- "Show all Data Science students"
  ```sql
  SELECT * FROM STUDENT where COURSE="Data Science";
  ```

## 🛠️ Technical Details

### Dependencies
- streamlit
- langchain-groq
- python-dotenv
- Groq API access

### Model
- Using llama3-8b-8192 model through Groq's API

### Features
- Natural language input
- Real-time SQL query generation
- User-friendly web interface
- Secure API key handling

## 📚 Usage

1. Launch the application
2. Enter your question in plain English
3. Click "Submit"
4. Get your SQL query instantly

## ⚙️ Configuration

Create a `.env` file in your project root:
```bash
GROQ_API_KEY=your_key_here
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request


---
Made with ❤️ using Streamlit and Groq