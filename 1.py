#Phạm Hoàng Tú
#MSV 2020606982
# arr = np.array([[1, 5, 6],
#                 [4, 7, 2],
#                 [3, 1, 9]])
# print("Largest element is: ", arr.max)
# print("Row-wise maximum elements: " arr.max(axis = 1))
# print("Column-wise minumun elements: ", arr.min(axis = 0))
# print("Sum of all array elements: ", arr.sum())
# print("Cumulative sum along each row: \n", arr.cumsum(axis = 1))
# Thêm nút chuyển vị và đảo ngược ma trận, thêm nhập ma trận từ file .xls, .xlsx

import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class ỨngDụngMaTrận:
    def __init__(self, chủ):
        self.chủ = chủ
        chủ.title("Các Phép Toán Trên Ma Trận")

        self.nhãn_hàng = tk.Label(chủ, text="Nhập số hàng:")
        self.đầu_vào_hàng = tk.Entry(chủ)
        self.nhãn_cột = tk.Label(chủ, text="Nhập số cột:")
        self.đầu_vào_cột = tk.Entry(chủ)
        self.nút_nhập = tk.Button(chủ, text="Nhập Ma Trận", command=self.nhập_ma_trận)
        self.nút_file_excel = tk.Button(chủ, text="Nhập Ma Trận Từ File Excel", command=self.nhập_ma_trận_từ_file)
        self.nút_thoát = tk.Button(chủ, text="Thoát", command=self.thoát_ứng_dụng)

        self.nhãn_hàng.pack()
        self.đầu_vào_hàng.pack()
        self.nhãn_cột.pack()
        self.đầu_vào_cột.pack()
        self.nút_nhập.pack()
        self.nút_file_excel.pack()
        self.nút_thoát.pack()

        # Thêm biến để lưu trữ ma trận đã nhập và cửa sổ kết quả
        self.ma_trận_nhập = None
        self.cửa_sổ_kết_quả = None

    def nhập_ma_trận(self):
        try:
            hàng = int(self.đầu_vào_hàng.get())
            cột = int(self.đầu_vào_cột.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ cho hàng và cột.")
            return

        # Tạo một đối tượng NhậpMaTrận và lưu trữ nó trong biến
        self.ma_trận_nhập = NhậpMaTrận(self.chủ, hàng, cột, self)

        # Hiển thị ma trận ngay sau khi nhập

    def nhập_ma_trận_từ_file(self):
        try:
            file_path = filedialog.askopenfilename(title="Chọn File Excel", filetypes=[("Excel files", "*.xlsx;*.xls")])
            if file_path:
                df = pd.read_excel(file_path, header=None)

                # Kiểm tra từng ô xem có phải là số nguyên hay không
                if not df.applymap(lambda x: isinstance(x, (int, np.int64, float, np.float64))).all().all():
                    messagebox.showerror("Lỗi", "File Excel chứa giá trị không hợp lệ. Vui lòng chỉ nhập số nguyên.")
                    return

                self.đầu_vào_hàng.delete(0, tk.END)
                self.đầu_vào_cột.delete(0, tk.END)
                self.đầu_vào_hàng.insert(0, df.shape[0])
                self.đầu_vào_cột.insert(0, df.shape[1])

                # Tạo một đối tượng NhậpMaTrận và lưu trữ nó trong biến
                self.ma_trận_nhập = NhậpMaTrận(self.chủ, df.shape[0], df.shape[1], self, ma_trận=df.values)

                # Hiển thị ma trận ngay sau khi nhập từ file
                self.ma_trận_nhập.hiển_thị_ma_trận()

        except pd.errors.ParserError:
            messagebox.showerror("Lỗi", "File Excel không đúng định dạng. Vui lòng chọn một file Excel hợp lệ.")

    def hiển_thị_ma_trận(self):
        if self.ma_trận_nhập:
            self.ma_trận_nhập.hiển_thị_ma_trận()

    def thoát_ứng_dụng(self):
        self.chủ.destroy()
class NhậpMaTrận:
    def __init__(self, chủ, hàng, cột, ứng_dụng_chính, ma_trận=None):
        self.chủ = chủ
        self.hàng = hàng
        self.cột = cột
        self.ứng_dụng_chính = ứng_dụng_chính

        if ma_trận is not None:
            self.ma_trận = ma_trận
        else:
            self.ma_trận = np.zeros((hàng, cột), dtype=int)
            self.xây_dựng_ma_trận()

    def xây_dựng_ma_trận(self):
        self.khung_đầu_vào = tk.Toplevel(self.chủ)
        self.khung_đầu_vào.title("Nhập Ma Trận")
        self.lưới_đầu_vào = [[None] * self.cột for _ in range(self.hàng)]

        for i in range(self.hàng):
            for j in range(self.cột):
                nhãn = tk.Label(self.khung_đầu_vào, text=f"({i+1}, {j+1}):")
                đầu_vào = tk.Entry(self.khung_đầu_vào)
                nhãn.pack(row=i, column=j * 2, padx=5, pady=5)
                đầu_vào.pack(row=i, column=j * 2 + 1, padx=5, pady=5)
                self.lưới_đầu_vào[i][j] = đầu_vào

        nút_gửi = tk.Button(self.khung_đầu_vào, text="Gửi", command=self.gửi_ma_trận)
        nút_gửi.pack(row=self.hàng, columnspan=self.cột * 2, pady=10)

    def gửi_ma_trận(self):
        for i in range(self.hàng):
            for j in range(self.cột):
                try:
                    self.ma_trận[i, j] = int(self.lưới_đầu_vào[i][j].get())
                except ValueError:
                    messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ cho tất cả các phần tử ma trận.")
                    return

        self.khung_đầu_vào.destroy()

        # Sau khi nhập ma trận, hiển thị menu
        self.hiển_thị_menu()

    def hiển_thị_ma_trận(self):
        if np.any(self.ma_trận):
            self.cửa_sổ_ma_trận = tk.Toplevel(self.chủ)
            self.cửa_sổ_ma_trận.title("Ma Trận Đã Nhập")

            tk.Label(self.cửa_sổ_ma_trận, text=np.array2string(self.ma_trận)).pack()

            # Tăng kích thước cửa sổ ma trận
            self.cửa_sổ_ma_trận.geometry("200x200")

        self.hiển_thị_menu()


    def hiển_thị_menu(self):
        khung_menu = tk.Toplevel(self.chủ)
        khung_menu.geometry("400x300")
        khung_menu.title("Các Phép Toán Trên Ma Trận")
        phép_toán_ma_trận = [
            ("Tìm phần tử lớn nhất trong ma trận", self.ma_trận.max),
            ("Tìm phần tử lớn nhất theo từng hàng", lambda: self.ma_trận.max(axis=1)),
            ("Tìm phần tử nhỏ nhất theo từng cột", lambda: self.ma_trận.min(axis=0)),
            ("Tính tổng tất cả phần tử của ma trận", lambda: self.ma_trận.sum()),
            ("Tính tổng tích lũy theo từng hàng", lambda: self.ma_trận.cumsum(axis=1)),
            ("Chuyển Vị Ma Trận", lambda: np.transpose(self.ma_trận)),
            ("Đảo Ngược Ma Trận", lambda: np.flip(self.ma_trận)),
        ]

        for i, (lựa_chọn, hàm) in enumerate(phép_toán_ma_trận, start=1):
            nút_lựa_chọn = tk.Button(khung_menu, text=f"{i}. {lựa_chọn}", command=lambda f=hàm: self.hiển_thị_kết_quả(f))
            nút_lựa_chọn.pack(pady=5)

        nút_thoát = tk.Button(khung_menu, text="Thoát", command=khung_menu.destroy)
        nút_thoát.pack(pady=5)

    def hiển_thị_kết_quả(self, hàm):
        kết_quả = hàm()

        # Nếu cửa sổ kết quả chưa được tạo, tạo nó
        if not self.ứng_dụng_chính.cửa_sổ_kết_quả:
            self.ứng_dụng_chính.cửa_sổ_kết_quả = tk.Toplevel(self.chủ)
            self.ứng_dụng_chính.cửa_sổ_kết_quả.title("Kết Quả")
        else:
            # Nếu đã tồn tại, xóa nội dung cũ
            for widget in self.ứng_dụng_chính.cửa_sổ_kết_quả.winfo_children():
                widget.destroy()

        # Hiển thị kết quả trong cửa sổ kết quả
        tk.Label(self.ứng_dụng_chính.cửa_sổ_kết_quả, text=np.array2string(kết_quả)).pack()
        self.ứng_dụng_chính.cửa_sổ_kết_quả.geometry("200x200")
def chạy_chương_trình():
    gốc = tk.Tk()
    ứng_dụng = ỨngDụngMaTrận(gốc)
    gốc.mainloop()

if __name__ == "__main__":
    chạy_chương_trình()
