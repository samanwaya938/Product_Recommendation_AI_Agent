from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.firecrawl import FirecrawlTools
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
FIRECRAWL_API_KEY = os.environ.get('FIRECRAWL_API_KEY')

os.environ['GEMINI_API_KEY'] = GEMINI_API_KEY
os.environ['FIRECRAWL_API_KEY'] = FIRECRAWL_API_KEY 

agent = Agent(
  name = 'Shopping Partner',
  model=Gemini(id='gemini-2.0-flash-exp'),
  tools=[FirecrawlTools()],
  instructions=[
        "You are a product recommender agent specializing in finding products that match user preferences.",
        "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%.",
        "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, Meesho, Nike, and other reputable platforms.",
        "Verify that each product recommendation is in stock and available for purchase.",
        "Avoid suggesting counterfeit or unverified products.",
        "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
        "Please include a link to the product page on the website.",
        "Format the recommendations neatly and ensure clarity for ease of user understanding.",
        "Ensure that the recommended products are in the same category as the user's preferences.",
        "Do not recommend products that are not suitable for the user's preferences.",]

)

# agent.print_response("Please suggest me Jeans for men within Rs.1000", stream=True)

st.title("Shopping Partner")

user_input = st.text_input("Enter your requirements:")

if st.button("Submit"):
    response = agent.print_response(user_input)
    if response:  # Check if the response is not None
        st.write(response)
    else:
        st.write("No response received. Please try again.")

  