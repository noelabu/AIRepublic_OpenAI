import streamlit as st
from streamlit_option_menu import option_menu

from ai_republic import AIRepublicActivity


# Sidebar for navigation and API key input
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
air = AIRepublicActivity(api_key=api_key)

with st.sidebar:
    page = option_menu(
        "Dashboard",
        ["Home", "About Me","Sentiment Analysis", "News Summarizer Tool"],
        icons=['house', 'info-circle', 'emoji-smile', 'file-text'],
        menu_icon="list",
        default_index=0,
    )

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to use the application.")

else:
    if page == "Home":
        st.title("News Summarizer and Sentiment Analysis Tool")
        st.write("Welcome to the News Summarizer and Sentiment Analysis Tool. This comprehensive platform provides clear, concise summaries of news articles and evaluates the sentiment of movie reviews, helping you quickly understand essential information and public opinion.")

        st.write("## What the Tool Does")
        st.write("This tool offers two key functionalities:")
        st.write("- **News Summarization:** Analyzes full-length news articles from a provided link, extracting critical information and presenting it in a structured format.")
        st.write("- **Sentiment Analysis:** Evaluates the emotional tone of movie reviews, categorizing sentiments as positive or negative.")

        st.write("## How It Works")
        st.write("### News Summarization")
        st.write("1. **Input the Article Link:** Provide the link to the news article.")
        st.write("2. **Analyze and Extract Information:** The tool scans the article, identifying key elements such as the main event, people involved, dates, locations, and supporting evidence.")
        st.write("3. **Structure the Summary:** It organizes the extracted information into a clear format, including:")
        st.write("   - **Headline:** A brief, engaging headline.")
        st.write("   - **Summary:** A short summary of the news article.")

        st.write("### Sentiment Analysis")
        st.write("1. **Input the Movie Review:** Provide the text of the movie review.")
        st.write("2. **Text Analysis:** The tool analyzes the language of the review, identifying keywords and phrases.")
        st.write("3. **Sentiment Analysis:** It categorizes the tone as positive or negative")

        st.write("## Why Use This Tool?")
        st.write("- **Time-Saving:** Quickly grasp the key points of news articles and understand movie sentiments.")
        st.write("- **Objective and Neutral:** Presents factual information and emotional analysis without bias.")
        st.write("- **Structured and Consistent:** Organized formats help users easily find relevant information.")

        st.write("## Ideal Users")
        st.write("This tool is perfect for:")
        st.write("- Busy professionals who need to stay informed about news and entertainment.")
        st.write("- Students and researchers looking for quick, accurate summaries and sentiment analysis.")
        st.write("- Media outlets and marketers wanting to understand public reactions to news and films.")

        st.write("Start using the News Summarizer and Sentiment Analysis Tool today to gain concise insights into the news and movie reviews that matter most!")

    elif page == "About Me":
        st.header("About Me")
        st.markdown("""
        Hi! I'm Noela Jean Bunag, a Python Developer and AI Enthusiast. I'm passionate about creating accessible AI solutions and exploring the possibilities of Natural Language Processing.
        
        Connect with me on [LinkedIn](https://www.linkedin.com/in/noela-bunag/) to discuss AI, Python development, or potential collaborations.
        
        Check out my portfolio at [noelabu.github.io](https://noelabu.github.io/) to see more of my projects and work.
        """)

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