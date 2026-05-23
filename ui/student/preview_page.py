import customtkinter as ctk


class StudentPreviewPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Student Preview",
            font=("Segoe UI", 42, "bold")
        )
        title.pack(
            pady=(60, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Preview academic prediction instantly",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )
        subtitle.pack()