import customtkinter as ctk
from PIL import Image


class LoginTemplate(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        role_name,
        accent_color,
        accent_hover,
        accent_bg,
        icon_path,
        hero_title,
        hero_subtitle,
        login_command
    ):
        super().__init__(parent, fg_color="#031126")

        self.login_command = login_command
        self.password_visible = False

        self.build_ui(
            role_name,
            accent_color,
            accent_hover,
            accent_bg,
            icon_path,
            hero_title,
            hero_subtitle
        )

    # ======================================
    # PASSWORD TOGGLE
    # ======================================
    def toggle_password(self):

        self.password_visible = not self.password_visible

        self.password_entry.configure(
            show="" if self.password_visible else "●"
        )

        self.eye_btn.configure(
            text="🙈" if self.password_visible else "👁"
        )

    # ======================================
    # BUTTON POP ANIMATION
    # ======================================
    def animate_button(self, button):

        button.configure(
            width=355,
            height=58
        )

        self.after(
            90,
            lambda: button.configure(
                width=370,
                height=62
            )
        )

    # ======================================
    # UI
    # ======================================
    def build_ui(
        self,
        role_name,
        accent_color,
        accent_hover,
        accent_bg,
        icon_path,
        hero_title,
        hero_subtitle
    ):

        # ======================================
        # MAIN LAYOUT
        # ======================================
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(0, weight=1)

        # ======================================
        # LEFT SECTION
        # ======================================
        left_section = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        left_section.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(20, 0),
            pady=45
        )

        # ======================================
        # LOGIN FORM
        # ======================================
        form = ctk.CTkFrame(
            left_section,
            width=480,
            height=720,
            fg_color="#F8FAFC",
            corner_radius=58,
            border_width=1,
            border_color="#E2E8F0"
        )

        form.pack()
        form.pack_propagate(False)

        # ======================================
        # APP TITLE
        # ======================================
        title = ctk.CTkLabel(
            form,
            text="EduVision AI",
            font=("Segoe UI", 32, "bold"),
            text_color="#0F172A"
        )
        title.pack(pady=(42, 28))

        # ======================================
        # ICON
        # ======================================
        icon_bg = ctk.CTkFrame(
            form,
            width=125,
            height=125,
            corner_radius=62,
            fg_color=accent_bg
        )
        icon_bg.pack()

        icon = ctk.CTkImage(
            light_image=Image.open(icon_path),
            dark_image=Image.open(icon_path),
            size=(68, 68)
        )

        icon_label = ctk.CTkLabel(
            icon_bg,
            image=icon,
            text=""
        )

        icon_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ======================================
        # LOGIN TITLE
        # ======================================
        login_title = ctk.CTkLabel(
            form,
            text=f"{role_name} Login",
            font=("Segoe UI", 30, "bold"),
            text_color="#0F172A"
        )

        login_title.pack(pady=(26, 8))

        subtitle = ctk.CTkLabel(
            form,
            text="Secure access to dashboard",
            font=("Segoe UI", 18),
            text_color="#64748B"
        )

        subtitle.pack(pady=(0, 36))

        # ======================================
        # USERNAME INPUT
        # ======================================
        self.username_entry = ctk.CTkEntry(
            form,
            width=370,
            height=60,
            corner_radius=30,
            placeholder_text="Username",
            border_width=1,
            border_color="#CBD5E1",
            fg_color="#FFFFFF",
            text_color="#0F172A",
            font=("Segoe UI", 16)
        )

        self.username_entry.pack()

        # ======================================
        # PASSWORD INPUT
        # ======================================
        password_frame = ctk.CTkFrame(
            form,
            fg_color="transparent"
        )

        password_frame.pack(pady=(22, 0))

        self.password_entry = ctk.CTkEntry(
            password_frame,
            width=290,
            height=60,
            corner_radius=30,
            placeholder_text="Password",
            show="●",
            border_width=1,
            border_color="#CBD5E1",
            fg_color="#FFFFFF",
            text_color="#0F172A",
            font=("Segoe UI", 16)
        )

        self.password_entry.pack(
            side="left",
            padx=(0, 12)
        )

        self.eye_btn = ctk.CTkButton(
            password_frame,
            text="👁",
            width=60,
            height=60,
            corner_radius=30,
            fg_color="#E2E8F0",
            hover_color="#CBD5E1",
            text_color="#0F172A",
            command=self.toggle_password
        )

        self.eye_btn.pack(side="left")

        # ======================================
        # LOGIN BUTTON
        # ======================================
        login_btn = ctk.CTkButton(
            form,
            text="LOGIN",
            width=370,
            height=62,
            corner_radius=32,
            fg_color=accent_color,
            hover_color=accent_hover,
            font=("Segoe UI", 20, "bold"),
            command=lambda: [
                self.animate_button(login_btn),
                self.login_command()
            ]
        )

        login_btn.pack(pady=(42, 0))

        # ======================================
        # FOOTER
        # ======================================
        footer = ctk.CTkLabel(
            form,
            text="EduVision AI Secure Access",
            font=("Segoe UI", 14),
            text_color="#64748B"
        )

        footer.pack(
            side="bottom",
            pady=(0, 22)
        )

        # ======================================
        # RIGHT SECTION
        # ======================================
        right_section = ctk.CTkFrame(
            self,
            fg_color="#050505"
        )

        right_section.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        hero = ctk.CTkFrame(
            right_section,
            fg_color="transparent"
        )

        hero.place(
            relx=0.08,
            rely=0.5,
            anchor="w"
        )

        hero_title_label = ctk.CTkLabel(
            hero,
            text=hero_title,
            font=("Segoe UI", 60, "bold"),
            text_color="white"
        )

        hero_title_label.pack(anchor="w")

        hero_subtitle_label = ctk.CTkLabel(
            hero,
            text=hero_subtitle,
            font=("Segoe UI", 24),
            text_color="#D1D5DB"
        )

        hero_subtitle_label.pack(
            anchor="w",
            pady=(10, 20)
        )

        line = ctk.CTkFrame(
            hero,
            width=180,
            height=5,
            fg_color=accent_color,
            corner_radius=999
        )

        line.pack(anchor="w")

        info = ctk.CTkLabel(
            hero,
            text=f"{role_name} portal powered by EduVision AI",
            font=("Segoe UI", 16),
            text_color="#94A3B8"
        )

        info.pack(
            anchor="w",
            pady=(22, 0)
        )