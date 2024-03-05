import wikipediaapi
import json
import csv
import os

from Helpfunctions import ask_gpt


def generate_qa_pairs_from_wikipedia(article_title, max_tokens=2048):
    # Set a user agent for the Wikipedia API requests
    wikipedia_headers = {'User-Agent': 'Your-User-Agent'}
    
    # Fetch content from the Wikipedia article
    wiki_wiki = wikipediaapi.Wikipedia('en', headers=wikipedia_headers)
    page_py = wiki_wiki.page(article_title)
    
    # Extract text content from the article
    article_content = page_py.text

    # Split the article into chunks of max_tokens
    chunks = [article_content[i:i + max_tokens] for i in range(0, len(article_content), max_tokens)]

    # Initialize an empty list to store generated QA pairs
    qa_list = []

    # Iterate over each chunk and generate QA pairs
    for i, chunk in enumerate(chunks):
        # Use GPT-3.5-turbo to generate questions and answers
        prompt = f"""# Task\nCreate as many question, reasoning and answer triplets as possible based on the Wikipedia article about {article_title} \n(article-Chunk {i + 1}/{len(chunks)}):\n{chunk}\n\n# Guidelines\nDo not ever mention the article in your reasoning, only known facts and conclusions from those that would lead you to your answer. Only add reasoning if it is absolutely necessary, otherwise leave it empty.\nOnly ask questions for which the answer is provided in the article-chunk and that have at least some relation to the game of chess. If absolutely no such questions can be asked just return an empty list.\nAll your question, reasoning, and answer pairs should be in a big valid list. Every item of the list should be a valid json dictionary containing the question, the reasoning, and the answer. Always use double quotes: "..." instead of single quotes: '...' for valid json both for the property names in the dictionary as well as for the strings(values).\n\n# Examples\n[{{"question":"How many pieces are there in a game of chess?", "reasoning":"The question is ambiguous; it does not specify whether it asks about distinct pieces or total pieces. Therefore, I am going to answer both possibilities.", "answer":"In a game of chess, there are 12 distinct pieces. Both the black player and the white player have: 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights, and 8 pawns. \\nThis means that in a game of chess, both players start with 16 pieces, for a total of 32 pieces."}},{{"question":"How old was Magnus Carlsen when he became world champion?", "reasoning":"Carlsen was born on the 30th of november of 1990 and he won his for world championship on the 26th of november of 2013 this means he would have been 22 years old.", "answer":"Magnus Carlsen was 22 years old when winning his first world championship."}},{{"question":"When was Magnus Carlsen born?", "reasoning":"", "answer":"He was born on 30 november 1990."}}]"""
        response = ask_gpt(prompt)
        # Parse the response string into a JSON object
        try:
            chunk_qa_pairs = json.loads(response)
        except:
            percentage = i/len(chunks)*100
            print(f"Soft fail at {percentage}% in article: {article_title}")
            response = ask_gpt(prompt)
            try:
                chunk_qa_pairs = json.loads(response)
            except:
                percentage = i/len(chunks)*100
                print(f"Hard fail at {percentage}% in article: {article_title}")
                return qa_list

        # Extend the generated QA pairs into the overall list
        qa_list.extend(chunk_qa_pairs)

    print(f"100% succesful in article: {article_title}")

    return qa_list

def extract_and_append_to_csv(data, csv_filename):
    # Check if the CSV file exists
    if os.path.isfile(csv_filename):
        # Read the CSV file to find the last used ID
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_ids = [int(row['Id']) for row in reader]

        # Determine the starting ID for new entries
        last_used_id = max(existing_ids)
        start_id = last_used_id + 1
    else:
        # If the file doesn't exist, start counting from 0
        start_id = 0

    # Append new data to the CSV file
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Id', 'Question', 'Reasoning', 'Reply']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If it's a new file, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Loop through the data and append to the CSV file
        for i, item in enumerate(data):
            writer.writerow({
                'Id': start_id + i,
                'Question': item['question'],
                'Reasoning': item['reasoning'],
                'Reply': item['answer']
            })

def get_linked_titles(article_title):
    # Set a user agent for the Wikipedia API requests
    wikipedia_headers = {'User-Agent': 'Your-User-Agent'}
    
    # Fetch content from the Wikipedia article
    wiki_wiki = wikipediaapi.Wikipedia('en', headers=wikipedia_headers)
    page_py = wiki_wiki.page(article_title)

    if not page_py.exists():
        return None

    linked_titles = [link.title for link in page_py.links.values()]
    return linked_titles

article_titles = ["List of chess players"]
linked_titles = get_linked_titles('List of chess players')
article_titles.extend(linked_titles)


for i, title in enumerate(article_titles):
    data = generate_qa_pairs_from_wikipedia(title)
    extract_and_append_to_csv(data, "Tasks/Task 1/Task_1.csv")
    print(f"{len(data)} qa-pairs added ({i+1}/{len(article_titles)})")
