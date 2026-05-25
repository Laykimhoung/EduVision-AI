import customtkinter as ctk

from ui.teacher.student_detail_page import StudentDetailPage


class StudentsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.build_ui()

    # ==================================
    # OPEN STUDENT DETAIL
    # ==================================
    def open_student_detail(self):

        for widget in self.master.winfo_children():
            widget.destroy()

        StudentDetailPage(
            self.master
        ).pack(
            fill="both",
            expand=True
        )

    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self,
            text="Students",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage student performance and monitor academic risk",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=35
        )

        # ==================================
        # TOP BAR
        # ==================================
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=25
        )

        search_entry = ctk.CTkEntry(
            top_bar,
            width=320,
            height=46,
            corner_radius=14,
            placeholder_text="Search student..."
        )

        search_entry.pack(side="left")

        class_dropdown = ctk.CTkComboBox(
            top_bar,
            values=[
                "Grade 12A",
                "Grade 12B",
                "Grade 11A",
                "Grade 11B"
            ],
            width=220,
            height=46,
            corner_radius=14,
            button_color="#EF4444",
            button_hover_color="#DC2626"
        )

        class_dropdown.set("Grade 12A")
        class_dropdown.pack(side="right")

        # ==================================
        # MAIN BODY
        # ==================================
        body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # ==================================
        # TABLE
        # ==================================
        table_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        table_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        table_title = ctk.CTkLabel(
            table_frame,
            text="Student List",
            font=("Segoe UI", 26, "bold")
        )

        table_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        # ==================================
        # TABLE HEADER
        # ==================================
        header = ctk.CTkFrame(
            table_frame,
            fg_color="#111827",
            corner_radius=18
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        columns = [
            ("ID", 80),
            ("Name", 180),
            ("Average", 120),
            ("Risk", 120),
            ("Action", 120)
        ]

        for col, width in columns:

            lbl = ctk.CTkLabel(
                header,
                text=col,
                width=width,
                font=("Segoe UI", 15, "bold")
            )

            lbl.pack(
                side="left",
                padx=5,
                pady=18
            )

        # ==================================
        # SCROLLABLE TABLE
        # ==================================
        scroll_table = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )

        scroll_table.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 20)
        )

        students = [
            ("001", "Dara", "84", "Low"),
            ("002", "Sokha", "54", "High"),
            ("003", "Lina", "72", "Medium"),
            ("004", "Nita", "91", "Low"),
            ("005", "Visal", "63", "Medium"),
            ("006", "Kimlong", "52", "High"),
            ("007", "Sophy", "88", "Low")
        ]

        for sid, name, avg, risk in students:

            row = ctk.CTkFrame(
                scroll_table,
                fg_color="#111827",
                corner_radius=18
            )

            row.pack(
                fill="x",
                pady=8,
                padx=5
            )

            if risk == "High":
                risk_color = "#EF4444"
            elif risk == "Medium":
                risk_color = "#F59E0B"
            else:
                risk_color = "#10B981"

            values = [
                (sid, 80),
                (name, 180),
                (avg, 120),
                (risk, 120)
            ]

            for value, width in values:

                lbl = ctk.CTkLabel(
                    row,
                    text=value,
                    width=width,
                    font=("Segoe UI", 15),
                    text_color=(
                        risk_color
                        if value == risk
                        else "#E5E7EB"
                    )
                )

                lbl.pack(
                    side="left",
                    padx=5,
                    pady=18
                )

            view_btn = ctk.CTkButton(
                row,
                text="View",
                width=100,
                height=38,
                corner_radius=12,
                fg_color="#EF4444",
                hover_color="#DC2626",
                command=self.open_student_detail
            )

            view_btn.pack(
                side="left",
                padx=8
            )

        # ==================================
        # PREVIEW PANEL
        # ==================================
        preview = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        preview.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        preview_title = ctk.CTkLabel(
            preview,
            text="Student Preview",
            font=("Segoe UI", 26, "bold")
        )

        preview_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        student_name = ctk.CTkLabel(
            preview,
            text="Dara",
            font=("Segoe UI", 30, "bold")
        )

        student_name.pack(
            anchor="w",
            padx=25
        )

        data = [
            ("Attendance", "92%"),
            ("Quiz", "84"),
            ("Homework", "81"),
            ("Assignment", "78"),
            ("Midterm", "75"),
            ("Final", "89"),
            ("Participation", "85"),
            ("Project", "90"),
            ("Behavior", "88")
        ]

        for key, value in data:

            row = ctk.CTkFrame(
                preview,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=25,
                pady=5
            )

            left = ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI", 15)
            )

            left.pack(side="left")

            right = ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI", 15, "bold")
            )

            right.pack(side="right")

        risk = ctk.CTkLabel(
            preview,
            text="LOW RISK",
            font=("Segoe UI", 20, "bold"),
            text_color="#10B981"
        )

        risk.pack(
            pady=25
        )