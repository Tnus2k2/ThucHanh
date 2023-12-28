import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, Tk, Label, Entry, Button
import pandas as pd
from random import sample, shuffle, random
from PIL import Image, ImageTk

class SinhVien:

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
            self.ds_de_thi = []  # Sử dụng biến thành viên của lớp
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
                SinhVien.ds_de_thi.append(de_thi)

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

def main():
    # Tạo cửa sổ chính của Tkinter
    root = tk.Tk()

    # Cung cấp các giá trị mẫu cho các đối số yêu cầu
    ho_ten = "John Doe"
    ma_sinh_vien = "12345"
    ma_lop = "CS101"
    ma_de = 1
    # Tạo một thể hiện của lớp SinhVien với các đối số được cung cấp
    sinh_vien_instance = SinhVien(root, ho_ten, ma_sinh_vien, ma_lop, ma_de)

    # Bắt đầu vòng lặp sự kiện Tkinter
    root.mainloop()

# Kiểm tra xem script có đang chạy trực tiếp không
if __name__ == "__main__":
    main()
