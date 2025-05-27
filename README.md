# Smart Research Assistant

A Python-based AI research assistant that leverages Hugging Face transformers and LangChain agentic AI to perform intelligent web searches, summarize information, and provide detailed answers to research queries. Results can also be exported as PDF reports.

![robo cover]((https://github.com/Lalith-Akash/Smart-Research-Assistant/blob/main/robo_cover.png))

# Features

AI-powered web search using DuckDuckGo

Summarization of long texts using Hugging Face models (facebook/bart-large-cnn)

Intelligent agent reasoning with LangChain

Interactive command-line interface

Export research results to PDF files

# Requirements

Python 3.8 or higher

API keys:

OpenAI API key (for language model calls)

# Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/smart-research-assistant.git
cd smart-research-assistant
```
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Set your OpenAI API key in the environment:

```bash
export OPENAI_API_KEY='your-openai-api-key'  # Windows: set OPENAI_API_KEY=your-openai-api-key
Usage
```
Run the app:

```bash
python smart_research_assistant.py
```
Enter a research topic when prompted.

The AI agent will perform web searches, summarize results, and provide an answer.

Optionally export the answer to a PDF file by typing y when asked.

Example
```vbnet
Enter a research topic (or 'exit' to quit): Climate change impacts on agriculture

Answer:
[Summarized and aggregated research text]

Export this answer to PDF? (y/n): y
PDF saved as Climate_change_impacts_on_agriculture.pdf
```
# Future Improvements

Web-based UI with Streamlit or Gradio

Voice input and audio summary

File upload support (PDFs, DOCX)

Citation and reference management

# Thank You! 