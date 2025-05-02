import tkinter as tk
from tkinter import messagebox
from game_logic import generate_numbers, check_answer

class MemoryGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.geometry("800x600")

        # Tạo khung
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Biến để lưu các số ngẫu nhiên và số lần chơi
        self.correct_numbers = generate_numbers()
        self.attempts = 3

        # Label hiển thị các số
        self.number_label = tk.Label(self.frame, text=self.correct_numbers, font=("Arial", 24))
        self.number_label.grid(row=0, column=0)

        # Nhập dữ liệu từ người dùng
        self.input_label = tk.Label(self.frame, text="Nhập các số cách nhau bằng dấu cách:")
        self.input_label.grid(row=1, column=0)

        self.entry = tk.Entry(self.frame, font=("Arial", 18))
        self.entry.grid(row=2, column=0)

        self.submit_button = tk.Button(self.frame, text="Xác nhận", command=self.check_input, font=("Arial", 18))
        self.submit_button.grid(row=3, column=0)

        # Đếm ngược thời gian
        self.countdown_label = tk.Label(self.frame, font=("Arial", 18))
        self.countdown_label.grid(row=4, column=0)
        self.countdown(10)

    def countdown(self, seconds):
        #hiển thị thời gian đếm ngược
        if seconds > 0:
            self.countdown_label.config(text=f"Thời gian còn lại: {seconds} giây")
            self.root.after(1000, self.countdown, seconds - 1)
        else:
            self.number_label.config(text="")

    def check_input(self):
        #Kiểm tra đáp án người dùng và hiển thị thông báo.
        user_input = self.entry.get()
        if check_answer(user_input, self.correct_numbers):
            if self.attempts > 1:
                self.attempts -= 1
                self.correct_numbers = generate_numbers()  # Tạo số mới cho vòng tiếp theo
                self.number_label.config(text=self.correct_numbers)
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Chính xác!", "Bạn đã nhập đúng! Vòng tiếp theo.")
            else:
                messagebox.showinfo("Chúc mừng!", "Chúc mừng bạn đã thắng trò chơi!")
                self.root.quit()
        else:
            messagebox.showerror("Sai rồi!", "Đáp án không đúng. Trò chơi kết thúc.")
            self.root.quit()