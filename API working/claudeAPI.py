import requests
import json



import os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("API_KEY")
def summarize_text(api_key, text):
    """
    Summarize text using Anthropic's Claude API
    """
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    # Updated request structure according to latest API specifications
    data = {
        "model": "claude-3-5-sonnet-20240620",
        "messages": [
            {
                "role": "user",
                "content": f"Please summarize this text: {text}"
            }
        ],
        "system": "You are a helpful AI assistant that summarizes text concisely.",
        "max_tokens": 1024  # Increased token limit for better summaries
    }

    try:
        response = requests.post(url, json=data, headers=headers)

        # Print response for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        response.raise_for_status()

        # Updated response parsing based on current API structure
        response_data = response.json()
        if 'content' in response_data:
            return response_data['content'][0]['text']
        else:
            return f"Unexpected response structure: {response_data}"

    except requests.exceptions.RequestException as e:
        return f"API call failed: {str(e)}"
    except json.JSONDecodeError:
        return "Failed to parse API response"


# Usage example
if __name__ == "__main__":
    api_key = api_key
    text = input("Enter the text you want to summarize: ")

    result = summarize_text(api_key, text)
    print("\nSummary:", result)