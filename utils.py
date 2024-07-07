import json as JS
import os as OS

ARTICLES_FILE ='articles.json'
ARTICLES_FOLDER = 'articles' 
DB_FOLDER = 'chroma_storage'
DATA_FOLDER = 'data'
EUROPEAN_ACT_URL='https://www.europarl.europa.eu/doceo/document/TA-9-2024-0138_EN.pdf'

# load articles data from file_name (.json)
def load_articles(file_name) -> list:
    result = []
    if OS.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                result = JS.load(file)
            except JS.JSONDecodeError:
                print("File exists but is not valid JSON. Returning empty object.")
    else:
        with open(file_name, 'w') as file:
            JS.dump('[{}]', file)
        print(f"File '{file_name}' did not exist and was created.")
        OS.mkdir('articles')
        print("'articles' directory was created")
    
    return result 

# save articles data to file_name (.json)
def save_articles(file_name, data):
    try:
        with open(file_name, 'w') as file:
            JS.dump(data, file, indent=4)
            print(f"Data successfully saved to '{file_name}'.")    
    except Exception as e:
        print(f"Error: trying to save articles data [{e}]")

# save articles content to individual files
def save_article_content(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"An IOError occurred: {e.strerror}")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Content successfully written to '{file_name}'.")

# load article body text from file 
def load_article_content(file_name):
    result = ''
    try:
        with open(file_name, 'r') as file:
            result = file.read()
    except Exception as e:
        print(f"An unexpected error occurred while reading content file '{file_name}': {e}")
    
    return result