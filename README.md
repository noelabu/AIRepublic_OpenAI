# AIRepublic_OpenAI

Welcome to the AIRepublic_OpenAI repository! This project is part of the Day 3 activity of the AI Republic AI First Bootcamp. It contains three interactive Jupyter notebooks that showcase various natural language processing (NLP) tools built using the OpenAI API and deployed with Streamlit. The notebooks included are:

1. **Chatbot**
2. **Sentiment Analysis**
3. **News Summarizer**

These applications utilize system prompts to guide the behavior of the OpenAI API, enhancing the functionality and user experience.

## Table of Contents

- [Installation](#installation)
- [Notebooks](#notebooks)
- [Usage](#usage)
- [API Key Configuration](#api-key-configuration)
- [Running the Streamlit App](#running-the-streamlit-app)
- [Contributing](#contributing)

## Installation

To get started, ensure you have the following installed:

- Python 3.10 or higher
- Pip

Clone the repository:

```bash
git clone https://github.com/noelabu/AIRepublic_OpenAI.git
cd AIRepublic_OpenAI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Notebooks

### 1. Chatbot
- **Notebook Name**: `AI_FIRST_DAY3_ACTIVITY1.ipynb`
- **Description**: This notebook demonstrates a simple conversational chatbot using the OpenAI API. Users can interact with the bot to simulate a conversation on various topics.

### 2. Sentiment Analysis
This notebook performs sentiment analysis on user-provided text. It leverages the OpenAI API to determine the sentiment (positive, negative, or neutral) of the input, using system prompts for improved accuracy.
- **Notebook Name**: `AI_FIRST_DAY3_ACTIVITY2.ipynb`
- **Description**: This notebook performs sentiment analysis on user-provided text. It leverages the OpenAI API to determine the sentiment (positive or negative) of the input, using system prompts for improved accuracy.

### 3. News Summarizer
- **Notebook Name**: `AI_FIRST_DAY3_ACTIVITY3.ipynb`
- **Description**:This tool summarizes news articles using the OpenAI API, making it easier for users to get the main points of a news story without reading the entire article. The summarization process is enhanced by system prompts.

## Usage

### API Key Configuration
To use the OpenAI API, you'll need an API key. Sign up at [OpenAI](https://openai.com) and create an API key. Store your key in an environment variable named `OPENAI_API_KEY`.

```bash
export OPENAI_API_KEY='your-api-key'
```

### Running the Streamlit App
After setting up the API key, you can run the Streamlit app to interact with the tools.

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to access the application. You can also access the application [here](https://noelabu-airepublicopenai.streamlit.app/).
## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.
