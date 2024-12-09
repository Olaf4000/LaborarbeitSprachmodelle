import json


def extract_content(original_json):
    """
    Extracts the desired format from the original JSON object.

    Args:
        original_json (dict): The original JSON object.

    Returns:
        dict: The extracted JSON in the desired format.
    """
    try:
        # Extract the "content" key as a string
        content_raw = original_json["choices"][0]["message"]["content"]

        # Parse the string into a JSON object
        content_json = json.loads(content_raw)

        # Return the extracted JSON
        return content_json

    except (KeyError, json.JSONDecodeError) as e:
        # Handle missing keys or invalid JSON
        print(f"Error extracting results: {e}")
        return {}

def extract_text(original_json):
    """
    Extracts the plain text from the 'content' key in the original JSON object.

    Args:
        original_json (dict): The original JSON object.

    Returns:
        str: The plain text from the 'content' key, or an empty string if an error occurs.
    """
    try:
        # Extract the "content" key as a string
        content_text = original_json["choices"][0]["message"]["content"]

        # Return the plain text
        return content_text

    except KeyError as e:
        # Handle missing keys
        print(f"Error extracting text: {e}")
        return ""