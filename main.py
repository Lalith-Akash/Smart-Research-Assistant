# Smart Research Assistant using Hugging Face + LangChain

from transformers import pipeline
from langchain.agents import Tool, initialize_agent
from langchain.llms import OpenAI
from langchain.tools import DuckDuckGoSearchRun
from fpdf import FPDF
import os

# Set API keys
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Load Hugging Face summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Define summarization function
def summarize_text(text):
    result = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return result[0]['summary_text']

# Define a tool for summarization
summarize_tool = Tool(
    name="Text Summarizer",
    func=summarize_text,
    description="Use this tool to summarize long articles or paragraphs."
)

# Define a web search tool using DuckDuckGo
search_tool = DuckDuckGoSearchRun()

# Initialize LangChain agent with tools
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[summarize_tool, search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Function to export result as PDF
def export_to_pdf(query, answer):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Research Topic: {query}\n\nAnswer:\n{answer}")
    filename = query.replace(" ", "_")[:50] + ".pdf"
    pdf.output(filename)
    print(f"PDF saved as {filename}")

# Simple interaction loop
def main():
    print("Welcome to the Smart Research Assistant!")
    while True:
        query = input("\nEnter a research topic (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        result = agent.run(query)
        print("\nAnswer:\n", result)

        export = input("\nExport this answer to PDF? (y/n): ")
        if export.lower() == 'y':
            export_to_pdf(query, result)

if __name__ == "__main__":
    main()
