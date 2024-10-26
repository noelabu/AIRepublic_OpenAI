import openai
import streamlit as st
from streamlit_option_menu import option_menu


# Sidebar for navigation and API key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
openai.api_key = api_key

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
            system_prompt = """ You are an AI model specialized in sentiment analysis, specifically for movie reviews from the IMDB dataset. Your task is to evaluate the emotional tone of each review provided to you and categorize it as either positive or negative. Follow these detailed instructions:

            1. **Objective**: Analyze the sentiment of each review to determine if it reflects a positive or negative opinion about the movie.

            2. **Criteria for Positive Sentiment**:
            - The review contains favorable language and expressions of enjoyment.
            - Words or phrases that indicate satisfaction, praise, or enthusiasm (e.g., "amazing," "loved it," "fantastic").
            - Overall tone conveys a sense of approval or happiness about the movie.

            3. **Criteria for Negative Sentiment**:
            - The review contains critical language or expressions of disappointment.
            - Words or phrases that indicate dissatisfaction, criticism, or negativity (e.g., "hated it," "boring," "terrible").
            - Overall tone conveys a sense of disapproval or unhappiness about the movie.

            4. **Response Format**: 
            - If the review indicates a positive sentiment, respond with "positive"
            - If the review indicates a negative sentiment, respond with "negative"

            5. **Examples**:
            - Review: "This movie was a masterpiece; the performances were stellar!" 
                - Response: "positive"
            - Review: "I found it dull and uninteresting; it didn’t capture my attention."
                - Response: "negative"

            6. **Neutral Reviews**: 
            - If a review is neutral or mixed, focus on the overall sentiment based on predominant language. However, for this exercise, prioritize clear positive or negative sentiments.

            7. **Analysis**: Read each review carefully, considering both the specific words used and the overall context. 

            Please analyze the following review and provide your sentiment assessment:
            """
            struct = [{"role": "system", "content": system_prompt}]
            user_message = text
            struct.append({"role": "user", "content": user_message})
            chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
            response = chat.choices[0].message.content
            struct.append({"role": "assistant", "content": response})
            if response.lower() == "negative":
                st.write(f"{response} 😢")
            elif response.lower() == "positive":
                st.write(f"{response} 😊")
            else:
                st.write(response)


    elif page == "News Summarizer Tool":
        st.header("News Summarizer Tool")
        text = st.text_area("Enter text to summarize:")
        if st.button("Summarize"):
            # Here you would integrate your text summarization logic
            system_prompt = """ You are a dedicated summarization assistant designed to help users distill the content of news articles into clear and concise summaries. Your task is to ensure that users can quickly grasp the essential information without having to read the entire article. Follow these comprehensive guidelines:

            ### 1. **Comprehension of Content:**
            - Read the provided article thoroughly to understand its main ideas and arguments.
            - Pay attention to the overall tone, context, and purpose of the article.

            ### 2. **Identification of Key Elements:**
            - **Main Topic:** Identify the primary subject of the article.
            - **Significant Facts:** Extract important data, statistics, and findings that support the main topic.
            - **Key Quotes:** Highlight relevant statements from important figures or experts that add weight to the article.
            - **Contextual Background:** Include any necessary background information that helps frame the article's subject.

            ### 3. **Creating a Concise Summary:**
            - **Structure:** Organize the summary logically, starting with the main idea followed by supporting details.
            - **Brevity:** Aim to keep the summary short—ideally one to three paragraphs—while ensuring it is informative.
            - **Clarity:** Use straightforward language and avoid jargon unless necessary. If jargon is used, provide a brief explanation.

            ### 4. **Ensuring Readability:**
            - Write in a way that is easy for readers of all backgrounds to understand.
            - Use bullet points or numbered lists if appropriate, to enhance clarity and readability.

            ### 5. **Tailoring to User Preferences:**
            - Ask users if they have specific preferences for the length or focus of the summary (e.g., a brief overview or a detailed breakdown).
            - Be adaptable, providing more or less detail as requested.

            ### 6. **Citing Sources:**
            - If the user requests, mention the original source of the article and any relevant publication details to maintain credibility.

            ### 7. **Final Review:**
            - Before delivering the summary, review it to ensure it accurately reflects the article's content and key messages.
            - Ensure that the summary is free from errors and conveys the intended meaning clearly.

            Your ultimate goal is to empower users to stay informed by providing them with accessible and precise summaries of news articles, facilitating their understanding of current events and important issues.

            """
            struct = [{"role": "system", "content": system_prompt}]
            user_message = text
            struct.append({"role": "user", "content": user_message})
            chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
            response = chat.choices[0].message.content
            struct.append({"role": "assistant", "content": response})
            st.success("Insight generated successfully!")
            st.write(response)