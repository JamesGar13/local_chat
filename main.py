from customtkinter import *

class RegistrationApp(CTk):
    def __init__(self):
        super().__init__()

        self.title("Форма реєстрації")
        self.geometry("400x350")
        self.resizable(False, False)

        self.title = CTkLabel(self, text="Створити акаунт", font=("Arial", 20, "bold"))
        self.title.pack(pady=15)

        self.user = CTkEntry(self, placeholder_text="Введіть ваш логін")
        self.user.pack(pady=10)

        self.email = CTkEntry(self, placeholder_text="Введіть ваш Email")
        self.email.pack(pady=10)

        self.password = CTkEntry(self, placeholder_text="Введіть пароль", show="*")
        self.password.pack(pady=10)

        self.btn = CTkButton(self, text="Зареєструватися", command=self.on_register_click)
        self.btn.pack(pady=15)

        self.status = CTkLabel(self, text="")
        self.status.pack(pady=5)

    def on_register_click(self):
        self.status.configure(text="Зачекайте...", text_color="gray")
        self.after(500, self.process_registration)

    def process_registration(self):
        username = self.user.get()
        email = self.email.get()
        password = self.password.get()

        if not username or not email or not password:
            self.status.configure(text="Заповніть усі поля!", text_color="red")
        else:
            self.status.configure(text=f"Успіх! Вітаємо, {username}!", text_color="green")


        self.after(3000, self.clear_status)

    def clear_status(self):
        self.status.configure(text="")


if __name__ == "__main__":
    app = RegistrationApp()
    app.mainloop()