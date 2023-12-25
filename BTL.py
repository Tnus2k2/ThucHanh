import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Ứng Dụng Bài Kiểm Tra")

        # Tạo biến để lưu trạng thái làm bài
        self.is_exam_done = False

        # Tạo các nút chuyển đến từng phần
        self.button_teacher = tk.Button(master, text="Giáo viên", command=self.goto_teacher)
        self.button_student = tk.Button(master, text="Sinh viên", command=self.goto_student)
        self.button_take_exam = tk.Button(master, text="Làm bài", command=self.goto_exam)
        self.button_result = tk.Button(master, text="Kết quả", command=self.goto_result)

        # Hiển thị nút Giáo viên ban đầu
        self.button_teacher.pack()

    def goto_teacher(self):
        self.hide_all_widgets()
        self.button_teacher.pack()

    def goto_student(self):
        self.hide_all_widgets()
        self.button_student.pack()

    def goto_exam(self):
        if not self.is_exam_done:
            self.hide_all_widgets()
            self.button_take_exam.pack()
        else:
            messagebox.showinfo("Thông Báo", "Bạn đã làm bài kiểm tra rồi.")

    def goto_result(self):
        if self.is_exam_done:
            self.hide_all_widgets()
            self.button_result.pack()
        else:
            messagebox.showinfo("Thông Báo", "Bạn cần làm bài kiểm tra trước.")

    def hide_all_widgets(self):
        self.button_teacher.pack_forget()
        self.button_student.pack_forget()
        self.button_take_exam.pack_forget()
        self.button_result.pack_forget()

    def set_exam_done(self):
        self.is_exam_done = True

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
