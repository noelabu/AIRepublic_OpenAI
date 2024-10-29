import openai
from newspaper import Article

class AIRepublicActivity:

    def __init__(self, api_key:str): 
        openai.api_key = api_key
        self.api_key = api_key

    def sentiment_analysis(self, review: str):
        """ Analyze the sentiment of a movie review and categorize it as positive or negative.

        This function utilizes the OpenAI API to assess the emotional tone of the provided movie review, 
        determining whether it expresses a positive or negative sentiment based on specified criteria.
    
        Args:
            review (str): the movie reviews to be categorized as "positive" or "negative"
        
        Returns:
            str: "positive" if the review reflects a favorable opinion, 
                 "negative" if it indicates a critical opinion.
        """

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
        struct.append({"role": "user", "content": review})
        chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
        response = chat.choices[0].message.content
        struct.append({"role": "assistant", "content": response})
        return response
    
    def news_scrape(self, news_url:str):
        """Scrape and parse a news article from the given URL.

        This function takes a URL of a news article, downloads the content, 
        and parses it to extract relevant information such as the title, 
        authors, publication date, and text.

        Args:
            news_url (str): The URL of the news article to scrape.

        Returns:
            Article: An Article object containing the parsed content of the news article.
        """
        article = Article(news_url)
        article.download()
        article.parse()
        return article

    def news_summarizer(self, content:str):
        """Summarize the content of a news article into a concise and clear overview.

        This function uses the OpenAI API to generate a summary of the provided news article, 
        allowing users to quickly grasp the essential information without reading the entire text.

        Args:
            content (str): The full text of the news article to be summarized.

        Returns:
            str: A concise summary of the article, highlighting the main ideas, significant facts, 
                and key quotes, organized for clarity and readability.
        """
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
        struct.append({"role": "user", "content": content})
        chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
        response = chat.choices[0].message.content
        struct.append({"role": "assistant", "content": response})
        return response
        
    
