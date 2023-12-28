import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, Tk, Label, Entry, Button
import pandas as pd
from random import sample, shuffle, random
from PIL import Image, ImageTk

class APP:
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
        self.button_back = tk.Button(master, text="Quay lại", command=self.back)
        self.button_back.pack(pady=10)

    def goto_login(self):
        self.hide_login_page()
        login = Dang_nhap_GV(self.master)

    def goto_register(self):
        self.hide_login_page()
        register_page = Dang_ky_GV(self.master)

    def hide_login_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def back(self):
        self.hide_login_page()
        login = Dang_nhap(self.master)


class Dang_ky_GV:
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
        # Đọc thông tin tài khoản từ file CSV GV (nếu có)
        try:
            df = pd.read_csv("GV_accounts.csv")
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
            new_account = pd.DataFrame({"Username": [username], "Password": [password]})
            df = pd.concat([df, new_account], ignore_index=True, sort=False)

            # Lưu DataFrame vào file CSV GV
            df.to_csv("GV_accounts.csv", index=False)

            messagebox.showinfo("Đăng Ký", "Đăng ký thành công!")

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goto_login(self):
        self.hide_page()
        login = Dang_nhap(self.master)

class Dang_nhap:
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
        self.button_exit = tk.Button(master, text="Thoat", command=self.exit, font=("Helvetica", 14), bd=0)
        self.button_exit.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

        # Cài đặt trọng tâm
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def goto_teacher(self):
        self.hide_first_page()
        teacher_page = APP(self.master)

    def goto_student(self):
        self.hide_first_page()
        student_page = Dang_Nhap_SV(self.master)

    def hide_first_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def exit(self):
        response = messagebox.askokcancel("Xác Nhận", "Bạn có chắc chắn muốn thoát?")
        if response:
            # Đóng cửa sổ
            self.master.destroy()


class Dang_nhap_GV:
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

        # Nút quay lại trang đăng nhập
        self.button_back = tk.Button(master, text="Quay Lại", command=self.goto_login)
        self.button_back.pack(pady=10)

    def goto_login(self):
        self.hide_page()
        login = APP(self.master)

    def login(self):
        # Đọc thông tin tài khoản từ file CSV
        df_gv = pd.read_csv("GV_accounts.csv")

        # Kiểm tra xem tài khoản có tồn tại không
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        # Kiểm tra tên đăng nhập và mật khẩu có tồn tại trong DataFrame không
        if any((df_gv['Username'].astype(str).str.lower() == username) & (
                df_gv['Password'].astype(str).str.lower() == password)):
            messagebox.showinfo("Đăng Nhập", "Đăng nhập thành công!")
            self.goto_teacher_page()
        else:
            messagebox.showerror("Đăng Nhập", "Sai tên đăng nhập hoặc mật khẩu.")

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goto_teacher_page(self):
        self.hide_page()
        teacher = Teacher(self.master)


class Dang_Nhap_SV:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Sinh Viên")
        # Tạo entry cho username và password
        self.label_name = tk.Label(master, text="Nhập họ và tên:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(master)
        self.entry_name.pack(pady=10)

        self.label_msv = tk.Label(master, text="Nhập mã sinh viên:")
        self.label_msv.pack(pady=10)
        self.entry_msv = tk.Entry(master, show="*")
        self.entry_msv.pack(pady=10)

        # Nút đăng nhập
        self.button_login = tk.Button(master, text="Đăng Nhập", command=self.goto_student_page)
        self.button_login.pack(pady=10)

        # Nút quay lại trang đăng nhập
        self.button_back = tk.Button(master, text="Quay Lại", command=self.goto_login)
        self.button_back.pack(pady=10)

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def login_student(self):
        student_accounts = SharedData.student_accounts
        username = self.entry_name.get().strip()
        msv = self.entry_msv.get().strip()

        for student_account in student_accounts:
            if student_account.username == username and student_account.msv == msv:
                messagebox.showinfo("Thông Báo", "Đăng nhập thành công!")
                self.hide_page()

                # Tạo một thể hiện của lớp Student và hiển thị cửa sổ sinh viên
                student = Student(self.master, student_account.username, student_account.msv, student_account.ma_lop,
                                  student_account.ma_de)
                break
        else:
            messagebox.showerror("Lỗi", "Đăng nhập thất bại. Kiểm tra lại thông tin đăng nhập.")

    def goto_student_page(self):
        self.login_student()

    def goto_login(self):
        self.hide_page()
        login = Dang_nhap(self.master)

class StudentAccount:
    def __init__(self, username, msv, ma_lop, ma_de):
        self.username = username
        self.msv = msv
        self.ma_lop = ma_lop
        self.ma_de = ma_de


class SharedData:
    student_accounts = []


class Teacher:
    def __init__(self, master):
        self.master = master
        self.master.title("Trang Giáo Viên")

        # Danh sách để lưu thông tin sinh viên và đề
        self.student_list = []
        self.exam_list = []

        # Tạo nút để thêm danh sách sinh viên từ file CSV
        self.button_add_student_list = tk.Button(master, text="Chọn File Sinh Viên",
                                                 command=self.choose_csv_student_file)
        self.button_add_student_list.pack(pady=10)

        # Tạo nút để thêm danh sách đề từ file CSV
        self.button_add_exam_list = tk.Button(master, text="Chọn File Đề", command=self.choose_csv_exam_file)
        self.button_add_exam_list.pack(pady=10)

        # Tạo nút để hiển thị thông tin sinh viên và đề
        self.button_show_info = tk.Button(master, text="Hiển Thị Thông Tin", command=self.show_info)
        self.button_show_info.pack(pady=10)

        # Nút quay lại trang đăng nhập
        self.button_back = tk.Button(master, text="Quay Lại", command=self.goto_login)
        self.button_back.pack(pady=10)

        self.csv_file_path = None

    def choose_csv_student_file(self):
        self.csv_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_DS = "DS_SV.csv"

        if self.csv_file_path:
            try:
                # Đọc thông tin sinh viên từ file CSV
                df_sv = pd.read_csv(self.file_DS, encoding='latin-1', engine='python')

                # Lặp qua từng dòng trong DataFrame và thêm vào danh sách sinh viên
                for index, row in df_sv.iterrows():
                    ho_ten = row['Ho_Ten']
                    ma_sinh_vien = row['Ma_Sinh_Vien']
                    ma_lop = row['Ma_Lop']
                    ma_de = row['Ma_De']

                    student = Student(self.master, ho_ten, ma_sinh_vien, ma_lop, ma_de)
                    self.student_list.append(student)

                    # Thêm exam_id vào danh sách self.exam_list
                    self.exam_list.append(ma_de)
                for student in self.student_list:
                    # Loại bỏ nút nhận đề
                    student.btn_chon_de_thi.destroy()
                    student.btn_lam_bai.destroy()
                # Hiển thị thông báo khi danh sách sinh viên được thêm thành công
                messagebox.showinfo("Thông Báo", "Thêm Danh Sách Sinh Viên từ file CSV thành công!")


                for index, row in df_sv.iterrows():
                    username = row['Ho_Ten']
                    msv = row['Ma_Sinh_Vien']
                    ma_lop = row['Ma_Lop']
                    ma_de = row['Ma_De']

                    student_account = StudentAccount(username, msv, ma_lop, ma_de)
                    SharedData.student_accounts.append(student_account)

            except FileNotFoundError:
                messagebox.showerror("Lỗi", "File CSV không tồn tại.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

        # Gọi hàm để sửa lỗi về nút nhận đề

    def get_student_accounts(self):
        return SharedData.student_accounts

    def choose_csv_exam_file(self):
        # Hiển thị hộp thoại lựa chọn tệp
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        file_De = "DE.csv"

        if file_path:
            try:
                # Đọc thông tin đề từ file CSV
                df_exam = pd.read_csv(file_De, encoding='latin-1', engine='python')

                # Lặp qua từng dòng trong DataFrame và thêm vào danh sách đề
                for index, row in df_exam.iterrows():
                    ma_de = row['Ma_De']
                    ten_de = row['Ten_De']
                    cau_hoi = row['Cau_Hoi']
                    dap_an_A = row['Dap_An_A']
                    dap_an_B = row['Dap_An_B']
                    dap_an_C = row['Dap_An_C']
                    dap_an_D = row['Dap_An_D']
                    dap_an_dung = row['Dap_An_Dung']

                    exam = DeThi(ma_de, ten_de, cau_hoi, dap_an_A, dap_an_B, dap_an_C, dap_an_D, dap_an_dung)
                    self.exam_list.append(exam)

                # Hiển thị thông báo khi danh sách đề được thêm thành công
                messagebox.showinfo("Thông Báo", "Thêm Danh Sách Đề từ file CSV thành công!")
            except FileNotFoundError:
                messagebox.showerror("Lỗi", "File CSV không tồn tại.")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

    def show_info(self):
        # Tạo một cửa sổ mới để hiển thị thông tin sinh viên và đề
        info_window = tk.Toplevel(self.master)
        info_window.title("Thông Tin Sinh Viên và Đề")
        info_window.geometry("400x400")
        # Tạo một Text widget để hiển thị nội dung của tệp CSV
        text_widget = tk.Text(info_window, height=10, width=50)
        text_widget.pack(pady=10)

        # Hiển thị thông tin sinh viên và đề trong Text widget
        text_widget.insert(tk.END, "Thông Tin Sinh Viên và Đề:\n\n")

        # Lặp qua danh sách sinh viên và hiển thị thông tin
        for student in self.student_list:
            text_widget.insert(tk.END,
                               f"Sinh Viên: {student.ho_ten}, Mã SV: {student.ma_sinh_vien}, Mã Lớp: {student.ma_lop}, Mã Đề: {student.ma_de}\n")

    def hide_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def goto_login(self):
        self.hide_page()
        login = Dang_nhap(self.master)


class Student:

    def __init__(self, master, ho_ten, ma_sinh_vien, ma_lop, ma_de):
        self.ho_ten = ho_ten
        self.ma_sinh_vien = ma_sinh_vien
        self.ma_lop = ma_lop
        self.ma_de = ma_de
        self.master = master
        self.master.title("Trang Sinh Viên")
        self.ds_de_thi = []
        # Thay đổi tên biến để tránh xung đột với tên của đối tượng
        self.btn_chon_de_thi = tk.Button(master, text="Chọn File Đề", command=self.load_ds_de_thi)
        self.btn_chon_de_thi.pack(pady=10)

        self.btn_lam_bai = tk.Button(master, text="Làm Bài", command=self.lam_bai)
        self.btn_lam_bai.pack(pady=10)

    def load_ds_de_thi(self):
        try:
            # Đọc thông tin đề từ file CSV
            df_de_thi = pd.read_csv("DE.csv", encoding='latin-1', engine='python')
            ma_de_value = self.ma_de
            # Lọc các câu hỏi có mã đề trùng với mã đề của sinh viên
            df_de_thi_sv = df_de_thi[df_de_thi['Ma_De'] == ma_de_value]
            # Lặp qua từng dòng trong DataFrame và thêm vào danh sách đề
            self.ds_de_thi = []
            for index, row in df_de_thi_sv.iterrows():
                ma_de = row['Ma_De']
                ten_de = row['Ten_De']
                cau_hoi = row['Cau_Hoi']
                dap_an_A = row['Dap_An_A']
                dap_an_B = row['Dap_An_B']
                dap_an_C = row['Dap_An_C']
                dap_an_D = row['Dap_An_D']
                dap_an_dung = row['Dap_An_Dung']

                de_thi = DeThi(ma_de, ten_de, cau_hoi, dap_an_A, dap_an_B, dap_an_C, dap_an_D, dap_an_dung)
                self.ds_de_thi.append(de_thi)

            messagebox.showinfo("Thông báo", "Đã tải danh sách đề thi thành công.")
            print(self.ds_de_thi)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "File DE.csv không tồn tại.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi đọc file DE.csv: {e}")


    def lam_bai(self):
        if not self.ds_de_thi:
            messagebox.showwarning("Cảnh báo", "Không có đề thi nào để làm.")
            return

        # Chọn ngẫu nhiên một đề thi từ danh sách
        de_thi_chon = random.choice(self.ds_de_thi)

        # Tạo một cửa sổ mới để hiển thị đề và câu hỏi
        cua_so_bai_thi = tk.Toplevel(self.master)
        cua_so_bai_thi.title("Làm Trắc Nghiệm")

        # Hiển thị tên đề và số điểm hiện tại
        tk.Label(cua_so_bai_thi, text=f"Đề: {de_thi_chon.ten_de}").pack()
        label_diem = tk.Label(cua_so_bai_thi, text="Điểm hiện tại: 0")
        label_diem.pack()

        # Lưu điểm
        diem = 0

        # Lặp qua tất cả 10 câu hỏi
        for i in range(10):
            # Hiển thị câu hỏi
            tk.Label(cua_so_bai_thi, text=f"Câu {i + 1}: {de_thi_chon.cau_hoi[i]}").pack()

            # Tạo radio buttons cho các đáp án
            var = tk.StringVar()
            for j, dap_an in enumerate(de_thi_chon.dap_an[i]):
                tk.Radiobutton(cua_so_bai_thi, text=dap_an, variable=var, value=j).pack()

            # Tạo nút để xác nhận và kiểm tra đáp án
            btn_xac_nhan = tk.Button(cua_so_bai_thi, text="Xác Nhận",
                                     command=lambda i=i, var=var: self.kiem_tra_dap_an(i, var, de_thi_chon,
                                                                                       cua_so_bai_thi, diem, label_diem,
                                                                                       btn_xac_nhan, btn_tiep_theo,
                                                                                       btn_hoan_thanh))
            btn_xac_nhan.pack()

        # Tạo nút để chuyển sang câu hỏi tiếp theo
        btn_tiep_theo = tk.Button(cua_so_bai_thi, text="Câu Tiếp Theo",
                                  command=lambda: self.cau_hoi_tiep_theo(btn_tiep_theo, btn_hoan_thanh, cua_so_bai_thi))
        btn_tiep_theo.pack_forget()

        # Tạo nút để hoàn thành bài thi
        btn_hoan_thanh = tk.Button(cua_so_bai_thi, text="Hoàn Thành",
                                   command=lambda: self.ket_thuc_bai_thi(btn_hoan_thanh, cua_so_bai_thi, diem))
        btn_hoan_thanh.pack_forget()
class DeThi:
    def __init__(self, ma_de, ten_de, cau_hoi, dap_an_A, dap_an_B, dap_an_C, dap_an_D, dap_an_dung):
        self.ma_de = ma_de
        self.ten_de = ten_de
        self.cau_hoi = cau_hoi
        self.dap_an_A = dap_an_A
        self.dap_an_B = dap_an_B
        self.dap_an_C = dap_an_C
        self.dap_an_D = dap_an_D
        self.dap_an_dung = [d['dap_an_dung'] for d in dap_an_dung]

def update_score():
    pass
def main():
    root = tk.Tk()
    login_page = Dang_nhap(root)
    root.mainloop()


def show_first_page(master):
    root = tk.Toplevel(master)
    first_page = Dang_nhap(root)


if __name__ == "__main__":
    main()
