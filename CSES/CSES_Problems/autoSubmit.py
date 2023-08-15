import os
import requests
from bs4 import BeautifulSoup

csrf_token=""
def get_csrf_token(session):
    url = 'https://cses.fi/login'
    soup = BeautifulSoup(session.get(url).content, 'html.parser')
    csrf_token = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']
    return csrf_token

def login_to_cses():
    login_data = {
        'nick': 'crawldata',
        'pass': '12345'
    }

    with requests.Session() as s:
        url = 'https://cses.fi/login'
        soup = BeautifulSoup(s.get(url).content, 'html.parser')
        csrf_token=soup.find(
            'input', attrs={'name': 'csrf_token'})['value']
        login_data['csrf_token'] = csrf_token
        r = s.post(url, data=login_data)
        return s
    
    
def submit_solution(session, problem_id, source_code):
    url = f"https://cses.fi/problemset/submit/{problem_id}/"
    # csrf_token = get_csrf_token(session)  # Lấy CSRF token từ trang submit

    data = {
        'csrfmiddlewaretoken': csrf_token,
        'lang': 'cpp',  # Thay thế bằng ngôn ngữ của mã của bạn
        'code': source_code
    }

    response = session.post(url, data=data)
    print("Enter submit site successfully!")
    print(response.text)  # In ra nội dung phản hồi từ server
    print(response.headers)

    # Kiểm tra xem việc nộp bài có thành công không
    if "Submission received!" in response.text:
        print(f"Nộp bài cho bài toán {problem_id} thành công.")
    else:
        print(f"Nộp bài cho bài toán {problem_id} thất bại.")

# Danh sách mã bài toán và tên tệp mã nguồn tương ứng
problem_files = {
    '1068': '1068 - Weird Algorithm.cpp',
    # Thêm các mã bài toán và tên tệp tương ứng nếu cần
}

if __name__ == "__main__":
    session = login_to_cses()
    for problem_id, file_name in problem_files.items():
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                source_code = file.read()
                submit_solution(session, problem_id, source_code)
        else:
            print(f"Không tìm thấy tệp {file_name}.")
