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

