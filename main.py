from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from input_related import url_ist, url_id
import os


def get_html_content(url, save_path='demo.html'):
    service = Service("C:/Users/DELL/Desktop/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    html = driver.page_source
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(html)
    driver.quit()


def read_html_file(file_path='demo.html'):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def parse_html_content(html):
    soup = BeautifulSoup(html, 'lxml')

    # Extract title
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.text if title_tag else "Untitled"

    # Extract div elements
    div_elements = soup.find_all('div', class_='td-post-content tagdiv-type')
    div_texts = [div.get_text(strip=True) for div in div_elements]

    return title, div_texts


def save_articles(url_id_, title, div_text):
    output_folder = 'text_output_file'
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, f"{url_id_}.txt")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(title + '\n')
        if div_text:  # Check if div_text is not empty
            output_file.write(div_text[0])


# Example usage
for i in range(len(url_id)):
    try:
        url = url_ist[i]
        get_html_content(url)
        html_content = read_html_file()
        title, div_texts = parse_html_content(html_content)
        save_articles(url_id[i], title, div_texts)
    except Exception as e:
        print(f"An error occurred for URL_ID {url_id[i]}: {str(e)}")

'''url = url_ist[13]
get_html_content(url)
html_content = read_html_file()
title, div_texts = parse_html_content(html_content)
save_articles(url_id[13], title, div_texts)'''







