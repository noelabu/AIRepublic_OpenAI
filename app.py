import streamlit as st
from streamlit_option_menu import option_menu

from ai_republic import AIRepublicActivity


# Sidebar for navigation and API key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
air = AIRepublicActivity(api_key=api_key)

with st.sidebar:
    page = option_menu(
        "Dashboard",
        ["Home", "About Us","Sentiment Analysis", "News Summarizer Tool"],
        icons=['house', 'info-circle', 'emoji-smile', 'file-text'],
        menu_icon="list",
        default_index=0,
    )

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to use the application.")

else:
    if page == "Home":
        st.header("Welcome to NLP Application")
        st.write("This application provides various Natural Language Processing features. Use the sidebar to navigate between different functionalities.")

    elif page == "About Us":
        st.header("About Us")
        st.write("We are a team dedicated to making NLP technologies accessible and easy to use. Our application leverages state-of-the-art models to provide chatbot, sentiment analysis, and text summarization capabilities.")

    elif page == "Sentiment Analysis":
        st.header("Sentiment Analysis")
        text = st.text_area("Enter text for sentiment analysis:")
        if st.button("Analyze Sentiment"):
            response = air.sentiment_analysis(review=text)
            if response.lower() == "negative":
                st.write(f"{response} 😢")
            elif response.lower() == "positive":
                st.write(f"{response} 😊")
            else:
                st.write(response)

    elif page == "News Summarizer Tool":
        st.header("News Summarizer Tool")
        text = st.text_input("Enter the link to news article:")
        if st.button("Summarize"):
            news = air.news_scrape(text)
            response = air.news_summarizer(news.text)
            st.success("Insight generated successfully!")
            st.subheader(news.title)
            st.write(response)