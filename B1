import tkinter as tk
import numpy as np

def giai_he_phuong_trinh():
    try:
        n = int(so_phuong_trinh_entry.get())
        A = [[float(matran_entries[i][j].get()) for j in range(n)] for i in range(n)]
        b = [float(vecto_b_entries[i].get()) for i in range(n)]

        x = np.linalg.solve(A, b)

        ket_qua_label.config(text="Nghiệm của hệ phương trình:")
        for i in range(n):
            ket_qua_label.config(text=ket_qua_label.cget("text") + f"\nx{i+1} = {x[i]}")
    except ValueError:
        ket_qua_label.config(text="Lỗi: Vui lòng nhập dữ liệu hợp lệ.")
    except np.linalg.LinAlgError:
        ket_qua_label.config(text="Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")

def them_phuong_trinh():
    global current_row
    n = int(so_phuong_trinh_entry.get())
    while current_row >= len(matran_entries):
        matran_entries.append([])

    # Sử dụng pack cho entry của phương trình
    entry_frame = tk.Frame(root)
    entry_frame.pack()
    for j in range(n):
        entryequation = tk.Entry(entry_frame)
        entryequation.pack(side="left")
        matran_entries[current_row].append(entryequation)

    # Sử dụng pack cho entry của vecto b
    entryvector = tk.Entry(entry_frame)
    entryvector.pack(side="left")
    vecto_b_entries.append(entryvector)

    current_row += 1

def xoa_phuong_trinh():
    global current_row
    if current_row > 0:
        # Hủy entry_frame
        entry_frame = matran_entries[current_row - 1][0].master
        entry_frame.destroy()
        matran_entries.pop()
        vecto_b_entries.pop()
        current_row -= 1
        ket_qua_label.config(text="")

# Tạo cửa sổ
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")
root.geometry("500x500")

# Nhập số lượng phương trình
so_phuong_trinh_label = tk.Label(root, text="Nhập số lượng phương trình n:")
so_phuong_trinh_label.pack()
so_phuong_trinh_entry = tk.Entry(root)
so_phuong_trinh_entry.pack()

# Khởi tạo danh sách cho ma trận A và vecto b
matran_entries = []
vecto_b_entries = []

# Dòng hiện tại trong giao diện
current_row = 0

# Nút thêm và xóa phương trình
them_button = tk.Button(root, text="Thêm phương trình", command=them_phuong_trinh)
them_button.pack()
xoa_button = tk.Button(root, text="Xóa phương trình", command=xoa_phuong_trinh)
xoa_button.pack()

# Nút giải hệ phương trình
giai_button = tk.Button(root, text="Giải", command=giai_he_phuong_trinh)
giai_button.pack()

# Kết quả
ket_qua_label = tk.Label(root, text="")
ket_qua_label.pack()

root.mainloop()
