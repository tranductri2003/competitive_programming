import os
import requests
from bs4 import BeautifulSoup

def get_source_code_from_github(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    file_elements = soup.select('td.content a')
    source_codes = {}

    for element in file_elements:
        file_name = element.get_text().strip()
        if file_name.endswith(".cpp"):  # Lọc chỉ lấy các file .cpp
            raw_url = element['href']
            raw_url = raw_url.replace('/blob', '')
            raw_url = "https://raw.githubusercontent.com" + raw_url
            source_code = requests.get(raw_url).text
            problem_id = file_name.split(" - ")[0]
            source_codes[problem_id] = source_code

    return source_codes

def login_to_cses():
    loginData = {
        'nick': 'crawldata',
        'pass': '12345'
    }
    with requests.Session() as s:
        url = 'https://cses.fi/login'
        soup = BeautifulSoup(s.get(url).content, 'html.parser')
        loginData['csrf_token'] = soup.find(
            'input', attrs={'name': 'csrf_token'})['value']
        r = s.post(url, data=loginData)
        return s

def submit_solution(session, problem_id, source_code):
    url = f"https://cses.fi/problemset/submit/{problem_id}/"
    data = {
        # 'csrfmiddlewaretoken': 'your_csrf_token_here',  # Replace with your CSRF token
        'lang': 'cpp',                                  # Replace with the language of your code
        'code': source_code
    }

    response = session.post(url, data=data)

    # Check if submission was successful
    if "Submission received!" in response.text:
        print(f"Solution for problem {problem_id} submitted successfully.")
    else:
        print(f"Submission for problem {problem_id} failed.")

# Replace 'your_github_url_here' with the URL of your GitHub repository
github_url = 'https://github.com/mrsac7/CSES-Solutions/tree/master/src'
source_codes = get_source_code_from_github(github_url)

if __name__ == "__main__":
    session = login_to_cses()

    for problem_id, source_code in source_codes.items():
        submit_solution(session, problem_id, source_code)

