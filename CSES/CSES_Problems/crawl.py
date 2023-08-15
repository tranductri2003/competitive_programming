# Import the required libraries
from bs4 import BeautifulSoup
import requests
import urllib.request
import os

# Function to create a folder if it does not exist


def folder(f_name):
    try:
        if not os.path.exists(f_name):
            os.makedirs(f_name)
    except OSError:
        print("The folder could not be created!")

# Function to get the list of questions from CSES problemset


def getQuestions():
    ques = dict()
    r = session.get(r'https://cses.fi/problemset/').content
    soup = BeautifulSoup(r, 'html.parser')
    for t in soup.find_all('li', class_='task'):
        quesID = t.a['href'].split('/')[-1]
        ques[quesID] = t.a.string
    return ques

# Function to create a session by logging in with username and password


def createSession(username, password):
    loginData = {
        'nick': username,
        'pass': password
    }
    with requests.Session() as s:
        url = 'https://cses.fi/login'
        soup = BeautifulSoup(s.get(url).content, 'html.parser')
        loginData['csrf_token'] = soup.find(
            'input', attrs={'name': 'csrf_token'})['value']
        r = s.post(url, data=loginData)
        return s

# Function to get the solution code and additional details of a question


def getSolution(ques, sol):
    r = session.get(sol).content
    soup = BeautifulSoup(r, 'html.parser')
    code = soup.find('pre', class_="linenums").get_text()
    return code, soup

# Function to find the correct solution URL for a question


def findCorrectSolution(ques):
    r = session.get(r"https://cses.fi/problemset/view/"+ques+"/").content
    soup = BeautifulSoup(r, 'html.parser')
    if int(soup.find('p').string.split()[-1]) == 0:  # No of submissions
        return None

    for link in soup.find_all('a', attrs={'class': 'details-link'}):
        sol = link['href']
        # get status of a solution
        res = soup.find('a', href=sol, class_='').span['class'][2]
        if res == 'full':
            return 'https://cses.fi'+sol
    return None


# Send a request to the CSES problemset page
response = requests.get("https://cses.fi/problemset/").content
soup = BeautifulSoup(response, 'html.parser')

# Ask for username and password
username = input('username: ')
password = input('password: ')

# Create a session by logging in with the provided username and password
session = createSession(username, password)

# If login is successful
if session:
    # Create a directory to store the files (if not exists)
    if not os.path.exists("CSES_Problems"):
        os.makedirs("CSES_Problems")

    # Get the list of questions
    questions = getQuestions()

    # Loop through each question
    for _ in questions:
        # Find the correct solution URL for the question
        sol = findCorrectSolution(_)
        if not sol:
            continue

        # Get the solution code and additional details of the question
        code, urls = getSolution(_, sol)

        # Counter for naming the files
        counter = 0
        for a in urls.select("div.samp-actions"):  # chạy qua từng testcase
            c = a.select("a.save")
            url = c[0].get("href")
            k = url.split("/")
            if (k[-3] == '1'):
                # Create a folder for each question
                folder(f"./{_}-{questions[_]}/")

                # Download input and output files for the question
                filename = f"./{_}-{questions[_]}/{counter//3}.inp"
                url = "https://cses.fi/" + url
                urllib.request.urlretrieve(url, filename)
            elif (k[-3] == '2'):
                # Create a folder for each question
                folder(f"./{_}-{questions[_]}/")

                # Download input and output files for the question
                filename = f"./{_}-{questions[_]}/{counter//3}.out"
                url = "https://cses.fi/" + url
                urllib.request.urlretrieve(url, filename)
            counter += 1

else:
    print("Exiting the program due to login failure.")
