import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook
from PIL import Image, ImageTk


class LoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Đăng Nhập")
        self.master.geometry("500x300")

        # Nút đăng nhập
        self.button_login = tk.Button(master, text="Đăng Nhập", command=self.goto_login)
        self.button_login.pack(pady=10)

        # Nút đăng ký
        self.button_register = tk.Button(master, text="Đăng Ký", command=self.goto_register)
        self.button_register.pack(pady=10)

        # Nút quay lại trang đầu tiên
        self.button_back = tk.Button(master, text="Quay Lại", command=show_first_page)
        self.button_back.pack(pady=10)
    def goto_login(self):
        self.hide_login_page()
        login = FirstPage(self.master)

    def goto_register(self):
        self.hide_login_page()
        register_page = Register(self.master)

    def hide_login_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

class Register:
    def __init__(self, master):
        self.master = master
        self.master.title("Phần Mềm Kiểm Tra Trách Nhiệm")
        self.master.geometry("500x500")  # Kích thước cửa sổ

        # Thêm hình ảnh đại diện cho giáo viên và học sinh
        image_teacher = Image.open("GV.png")
        image_teacher = image_teacher.resize((200, 200), resample=Image.BOX)
        self.teacher_image = ImageTk.PhotoImage(image_teacher)

        image_student = Image.open("HS.png")
        image_student = image_student.resize((200, 200), resample=Image.BOX)
        self.student_image = ImageTk.PhotoImage(image_student)

        # Hiển thị dòng văn bản ở đầu trang
        self.label_title = tk.Label(master, text="Phần Mềm Kiểm Tra Trách Nhiệm", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Hiển thị hình ảnh và nút giáo viên
        self.label_teacher = tk.Label(master, image=self.teacher_image, compound="top")
        self.label_teacher.grid(row=1, column=0, sticky="nsew")
        self.button_teacher = tk.Button(master, text="Giáo viên", command=self.goto_teacher_regis, font=("Helvetica", 14),
                                        bd=0)
        self.button_teacher.grid(row=2, column=0, sticky="nsew")

        # Hiển thị hình ảnh và nút học sinh
        self.label_student = tk.Label(master, image=self.student_image, compound="top")
        self.label_student.grid(row=1, column=1, sticky="nsew")
        self.button_student = tk.Button(master, text="Học sinh", command=self.goto_student_regis, font=("Helvetica", 14),
                                        bd=0)
        self.button_student.grid(row=2, column=1, sticky="nsew")

        # Hiển thị quay lại
        self.button_back = tk.Button(master, text="Quay Lại", command=self.back_page, font=("Helvetica", 14), bd=0)
        self.button_back.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

        # Cài đặt trọng tâm
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def goto_teacher_regis(self):
        self.hide_page()
        teacher_page = GV_RegisterPage(self.master)

    def goto_student_regis(self):
        self.hide_page()
        student_page = SV_RegisterPage(self.master)

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def back_page(self):
        self.hide_page()
        login_page = LoginPage(self.master)

class GV_RegisterPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Đăng Ký")
        self.master.geometry("500x300")

        # Tạo entry cho username và password
        self.label_username = tk.Label(master, text="Tên đăng nhập:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(master, text="Mật khẩu:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=10)

        # Nút đăng ký
        self.button_register = tk.Button(master, text="Đăng Ký", command=self.register)
        self.button_register.pack(pady=10)

        # Nút quay lại trang đăng nhập
        self.button_back = tk.Button(master, text="Quay Lại", command=self.goto_login)
        self.button_back.pack(pady=10)

    def register(self):
        # Đọc thông tin tài khoản từ file Excel (nếu có)
        try:
            df = pd.read_excel("GV_accounts.xlsx")
        except FileNotFoundError:
            # Nếu file không tồn tại, tạo một DataFrame mới
            df = pd.DataFrame(columns=["Username", "Password"])

        # Lấy thông tin từ entry
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra xem tài khoản có tồn tại không
        if not df[df['Username'] == username].empty:
            messagebox.showerror("Đăng Ký", "Tài khoản đã tồn tại.")
        else:
            # Thêm tài khoản mới vào DataFrame
            df = df = pd.concat([df, pd.DataFrame({"Username": [username], "Password": [password]})], ignore_index=True, sort=False)

            # Lưu DataFrame vào file Excel
            df.to_excel("accounts.xlsx", index=False)

            messagebox.showinfo("Đăng Ký", "Đăng ký thành công!")

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goto_login(self):
        self.hide_page()
        login = LoginPage(self.master)

class SV_RegisterPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Đăng Ký")
        self.master.geometry("500x300")

        # Tạo entry cho username và password
        self.label_username = tk.Label(master, text="Tên đăng nhập:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(master, text="Mật khẩu:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=10)

        # Nút đăng ký
        self.button_register = tk.Button(master, text="Đăng Ký", command=self.register)
        self.button_register.pack(pady=10)

        # Nút quay lại trang đăng nhập
        self.button_back = tk.Button(master, text="Quay Lại", command=self.goto_login)
        self.button_back.pack(pady=10)

    def register(self):
        # Đọc thông tin tài khoản từ file Excel (nếu có)
        try:
            df = pd.read_excel("SV_accounts.xlsx")
        except FileNotFoundError:
            # Nếu file không tồn tại, tạo một DataFrame mới
            df = pd.DataFrame(columns=["Username", "Password"])

        # Lấy thông tin từ entry
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra xem tài khoản có tồn tại không
        if not df[df['Username'] == username].empty:
            messagebox.showerror("Đăng Ký", "Tài khoản đã tồn tại.")
        else:
            # Thêm tài khoản mới vào DataFrame
            df = df = pd.concat([df, pd.DataFrame({"Username": [username], "Password": [password]})], ignore_index=True, sort=False)

            # Lưu DataFrame vào file Excel
            df.to_excel("accounts.xlsx", index=False)

            messagebox.showinfo("Đăng Ký", "Đăng ký thành công!")

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goto_login(self):
        self.hide_page()
        login = LoginPage(self.master)

class FirstPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Phần Mềm Kiểm Tra Trách Nhiệm")
        self.master.geometry("500x500")  # Kích thước cửa sổ

        # Thêm hình ảnh đại diện cho giáo viên và học sinh
        image_teacher = Image.open("GV.png")
        image_teacher = image_teacher.resize((200, 200), resample=Image.BOX)
        self.teacher_image = ImageTk.PhotoImage(image_teacher)

        image_student = Image.open("HS.png")
        image_student = image_student.resize((200, 200), resample=Image.BOX)
        self.student_image = ImageTk.PhotoImage(image_student)

        # Hiển thị dòng văn bản ở đầu trang
        self.label_title = tk.Label(master, text="Phần Mềm Kiểm Tra Trách Nhiệm", font=("Helvetica", 16))
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Hiển thị hình ảnh và nút giáo viên
        self.label_teacher = tk.Label(master, image=self.teacher_image, compound="top")
        self.label_teacher.grid(row=1, column=0, sticky="nsew")
        self.button_teacher = tk.Button(master, text="Giáo viên", command=self.goto_teacher, font=("Helvetica", 14),
                                        bd=0)
        self.button_teacher.grid(row=2, column=0, sticky="nsew")

        # Hiển thị hình ảnh và nút học sinh
        self.label_student = tk.Label(master, image=self.student_image, compound="top")
        self.label_student.grid(row=1, column=1, sticky="nsew")
        self.button_student = tk.Button(master, text="Học sinh", command=self.goto_student, font=("Helvetica", 14),
                                        bd=0)
        self.button_student.grid(row=2, column=1, sticky="nsew")

        # Hiển thị quay lại
        self.button_back = tk.Button(master, text="Quay Lại", command=self.back_page, font=("Helvetica", 14), bd=0)
        self.button_back.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

        # Cài đặt trọng tâm
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def goto_teacher(self):
        self.hide_first_page()
        teacher_page = TeacherPage(self.master)

    def goto_student(self):
        self.hide_first_page()
        student_page = StudentPage(self.master)

    def hide_first_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def back_page(self):
        if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn thoát không?"):
            self.hide_first_page()
            login_page = LoginPage(self.master)



class TeacherPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Giáo Viên")
        # Tạo entry cho username và password
        self.label_username = tk.Label(master, text="Tên đăng nhập:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(master, text="Mật khẩu:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=10)

        # Nút đăng nhập
        self.button_login = tk.Button(master, text="Đăng Nhập", command=self.login)
        self.button_login.pack(pady=10)
    def login(self):
        # Đọc thông tin tài khoản từ file Excel
        df = pd.read_excel("GV_accounts.xlsx")

        # Kiểm tra xem tài khoản có tồn tại không
        username = self.entry_username.get()
        password = self.entry_password.get()

        if df[(df['Username'] == username) & (df['Password'] == password)].empty:
            messagebox.showerror("Đăng Nhập", "Sai tên đăng nhập hoặc mật khẩu.")
        else:
            messagebox.showinfo("Đăng Nhập", "Đăng nhập thành công!")


class StudentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Giáo Viên")
        # Tạo entry cho username và password
        self.label_username = tk.Label(master, text="Tên đăng nhập:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=10)

        self.label_password = tk.Label(master, text="Mật khẩu:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=10)

        # Nút đăng nhập
        self.button_login = tk.Button(master, text="Đăng Nhập", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        # Đọc thông tin tài khoản từ file Excel
        df = pd.read_excel("SV_accounts.xlsx")

        # Kiểm tra xem tài khoản có tồn tại không
        username = self.entry_username.get()
        password = self.entry_password.get()

        if df[(df['Username'] == username) & (df['Password'] == password)].empty:
            messagebox.showerror("Đăng Nhập", "Sai tên đăng nhập hoặc mật khẩu.")
        else:
            messagebox.showinfo("Đăng Nhập", "Đăng nhập thành công!")


def main():
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()


def show_first_page(page):
    if page == "first_page":
        root = tk.Toplevel()
        first_page = FirstPage(root)

if __name__ == "__main__":
    main()
