import customtkinter as ctk


class AssessmentPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.build_ui()

    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self,
            text="Assessment",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Monitor academic performance and learning signals",
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
        class_dropdown.pack(side="left")

        search_entry = ctk.CTkEntry(
            top_bar,
            width=300,
            height=46,
            corner_radius=14,
            placeholder_text="Search student..."
        )

        search_entry.pack(side="right")

        # ==================================
        # SUMMARY CARDS
        # ==================================
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )

        stats = [
            ("81", "Quiz Avg", "#EF4444"),
            ("79", "Homework Avg", "#3B82F6"),
            ("74", "Midterm Avg", "#F59E0B"),
            ("84", "Final Avg", "#10B981")
        ]

        for value, label, color in stats:

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                height=145,
                corner_radius=28
            )

            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=10
            )

            num = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            )

            num.pack(
                pady=(28, 5)
            )

            txt = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            )

            txt.pack()

        # ==================================
        # BODY
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

        body.grid_columnconfigure(0, weight=3)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # ==================================
        # TABLE AREA
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
            text="Assessment Overview",
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
            ("Student", 140),
            ("Quiz", 70),
            ("HW", 70),
            ("Assign", 80),
            ("Mid", 70),
            ("Final", 70),
            ("Part.", 70),
            ("Project", 80),
            ("Behavior", 90)
        ]

        for col, width in columns:

            lbl = ctk.CTkLabel(
                header,
                text=col,
                width=width,
                font=("Segoe UI", 14, "bold")
            )

            lbl.pack(
                side="left",
                padx=4,
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
            ("Dara", 84, 81, 78, 75, 89, 85, 90, 88),
            ("Sokha", 54, 62, 58, 60, 57, 45, 59, 68),
            ("Lina", 76, 72, 74, 79, 80, 83, 82, 84),
            ("Nita", 92, 90, 91, 89, 94, 95, 93, 90),
            ("Visal", 61, 67, 65, 63, 70, 58, 72, 74),
            ("Kimlong", 50, 52, 58, 55, 60, 45, 59, 66)
        ]

        for student in students:

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

            values = [
                (student[0], 140),
                (student[1], 70),
                (student[2], 70),
                (student[3], 80),
                (student[4], 70),
                (student[5], 70),
                (student[6], 70),
                (student[7], 80),
                (student[8], 90)
            ]

            for value, width in values:

                color = "#E5E7EB"

                if isinstance(value, int):
                    if value < 60:
                        color = "#EF4444"
                    elif value < 75:
                        color = "#F59E0B"
                    else:
                        color = "#10B981"

                lbl = ctk.CTkLabel(
                    row,
                    text=str(value),
                    width=width,
                    font=("Segoe UI", 14),
                    text_color=color
                )

                lbl.pack(
                    side="left",
                    padx=4,
                    pady=18
                )

        # ==================================
        # RISK PANEL
        # ==================================
        risk_panel = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        risk_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        risk_title = ctk.CTkLabel(
            risk_panel,
            text="Academic Risk",
            font=("Segoe UI", 26, "bold")
        )

        risk_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        risk_students = [
            ("Sokha", "High Risk"),
            ("Kimlong", "High Risk"),
            ("Visal", "Medium Risk"),
            ("Lina", "Low Risk")
        ]

        for student, risk in risk_students:

            card = ctk.CTkFrame(
                risk_panel,
                fg_color="#111827",
                corner_radius=18
            )

            card.pack(
                fill="x",
                padx=20,
                pady=8
            )

            row = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=18,
                pady=18
            )

            student_name = ctk.CTkLabel(
                row,
                text=student,
                font=("Segoe UI", 17, "bold")
            )

            student_name.pack(side="left")

            if "High" in risk:
                color = "#EF4444"
            elif "Medium" in risk:
                color = "#F59E0B"
            else:
                color = "#10B981"

            risk_label = ctk.CTkLabel(
                row,
                text=risk,
                font=("Segoe UI", 15, "bold"),
                text_color=color
            )

            risk_label.pack(side="right")