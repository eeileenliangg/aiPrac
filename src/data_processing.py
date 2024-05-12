import requests
from bs4 import BeautifulSoup as bs

# Fetch from Merriam Webster
def fetch_example_sentence(word):
    url = f"https://www.merriam-webster.com/dictionary/{word}"
    try:
        r = requests.get(url)
        r.raise_for_status()  #
        soup = bs(r.content, 'lxml')
        example = soup.select_one('.ex-sent').get_text(separator=" ", strip=True)
        return example
    except requests.RequestException as e:
        print(f"Failed to fetch data for {word}: {e}")
        return []
    except Exception as e:
        print(f"Error processing data for {word}: {e}")
        return []

# Fetch from Urban Dictionary
def fetch_urban_sentence(word):
    url = f"https://www.urbandictionary.com/define.php?term={word}"
    try:
        r = requests.get(url)
        r.raise_for_status()  #
        soup = bs(r.content, 'lxml')
        preprocess = soup.find('div', class_='break-words example italic mb-4')
        postprocess = ''
        # Iterate over all contents of the div, extracting strings
        for content in preprocess.contents:
            if content.name == 'a':
                postprocess += content.text
            else:
                postprocess += content if isinstance(content, str) else ''
        postprocess = postprocess.replace('"', '')
        return postprocess
    except requests.RequestException as e:
        print(f"Failed to fetch data for {word}: {e}")
        return []
    except Exception as e:
        print(f"Error processing data for {word}: {e}")
        return []
    
# List of words to process
words = ["freezing", "heat", "rain", "sunshine", "windy"]  # Example words

# Collecting examples for each Merriam word
for word in words:
    example = fetch_example_sentence(word)
    print(f"Example for {word}: {example if example else 'No example found.'}")

# Collecting examples for each Urban word
for word in words:
    example = fetch_urban_sentence(word)
    print(f"Urban Example for {word}: {example if example else 'No example found.'}")