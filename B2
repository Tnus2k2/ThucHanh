import tkinter as tk


class AnalyticStudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Học tập Giải tích")

        # Giao diện chính
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Tiêu đề
        self.title_label = tk.Label(self.main_frame, text="Học Giải tích")
        self.title_label.pack()

        # Menu
        self.menu_frame = tk.Frame(self.main_frame)
        self.menu_frame.pack()

        self.exercise_button = tk.Button(self.menu_frame, text="Làm bài tập", command=self.start_exercise)
        self.exercise_button.pack(side="left")

        self.lecture_button = tk.Button(self.menu_frame, text="Xem bài giảng", command=self.open_lecture)
        self.lecture_button.pack(side="left")

        # Kết quả
        self.result_frame = tk.Frame(self.main_frame)
        self.result_frame.pack()
        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack()

    def start_exercise(self):
        # Gọi hàm để làm bài tập (Cần viết mã code cho tính năng làm bài tập)
        # Sau khi làm bài tập, cập nhật kết quả vào self.result_label
        self.result_label.config(text="Bài tập đã hoàn thành!")

    def open_lecture(self):
        # Gọi hàm để mở bài giảng (Cần viết mã code cho tính năng xem bài giảng)
        # Hiển thị nội dung bài giảng trong một cửa sổ mới hoặc trình duyệt mặc định
        self.result_label.config(text="Xem bài giảng...")


if __name__ == "__main__":
    root = tk.Tk()
    app = AnalyticStudyApp(root)
    root.mainloop()
