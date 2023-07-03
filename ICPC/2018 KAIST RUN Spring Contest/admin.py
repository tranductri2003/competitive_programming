import tkinter as tk
import ftplib

# Tạo đối tượng FTP và kết nối đến máy chủ
ftp = ftplib.FTP("192.168.56.1")
ftp.login("tritran", "1234")

# Hàm tải lên tệp


def upload_file():
    remote_file_path = remote_file_entry.get()
    local_file_path = local_file_entry.get()
    with open(local_file_path, "rb") as file:
        ftp.storbinary(f"STOR {remote_file_path}", file)
    status_label.config(text="File uploaded successfully!")

# Hàm tải xuống tệp


def download_file():
    remote_file_path = remote_file_entry2.get()
    local_file_path = local_file_entry2.get()
    with open(local_file_path, "wb") as file:
        ftp.retrbinary(f"RETR {remote_file_path}", file.write)
    status_label.config(text="File downloaded successfully!")


# Tạo cửa sổ chính và các thành phần của nó
root = tk.Tk()
root.title("FTP Uploader and Downloader")

# Thành phần cho tải lên tệp
remote_file_label = tk.Label(root, text="Remote File Path:")
remote_file_entry = tk.Entry(root)
local_file_label = tk.Label(root, text="Local File Path:")
local_file_entry = tk.Entry(root)
file_upload_button = tk.Button(root, text="Upload File", command=upload_file)

# Thành phần cho tải xuống tệp
download_label = tk.Label(root, text="Download File")
download_label.config(font=("Courier", 16))

remote_file_label2 = tk.Label(root, text="Remote File Path:")
remote_file_entry2 = tk.Entry(root)
local_file_label2 = tk.Label(root, text="Local File Path:")
local_file_entry2 = tk.Entry(root)
file_download_button = tk.Button(
    root, text="Download File", command=download_file)

status_label = tk.Label(root, text="")

# Định vị các thành phần trong cửa sổ
remote_file_label.grid(row=0, column=0)
remote_file_entry.grid(row=0, column=1)
local_file_label.grid(row=1, column=0)
local_file_entry.grid(row=1, column=1)
file_upload_button.grid(row=2, column=1)

download_label.grid(row=3, column=0, columnspan=2)
remote_file_label2.grid(row=4, column=0)
remote_file_entry2.grid(row=4, column=1)
local_file_label2.grid(row=5, column=0)
local_file_entry2.grid(row=5, column=1)
file_download_button.grid(row=6, column=1)

status_label.grid(row=7, column=0, columnspan=2)

root.mainloop()

# Đóng kết nối FTP
ftp.quit()
