import customtkinter as ctk


class ClassroomPage(ctk.CTkFrame):

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
            text="Classroom",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage classes and monitor classroom performance",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=35
        )

        # ==================================
        # CLASS SELECTOR
        # ==================================
        top_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_frame.pack(
            fill="x",
            padx=35,
            pady=28
        )

        current_label = ctk.CTkLabel(
            top_frame,
            text="Current Class",
            font=("Segoe UI", 17, "bold")
        )

        current_label.pack(
            side="left",
            padx=(0, 15)
        )

        class_dropdown = ctk.CTkComboBox(
            top_frame,
            values=[
                "Grade 12A",
                "Grade 12B",
                "Grade 11A",
                "Grade 11B"
            ],
            width=220,
            height=45,
            corner_radius=14,
            button_color="#EF4444",
            button_hover_color="#DC2626"
        )

        class_dropdown.set("Grade 12A")
        class_dropdown.pack(side="left")

        # ==================================
        # CLASS STATS
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
            ("42", "Students", "#EF4444"),
            ("91%", "Attendance", "#10B981"),
            ("84%", "Performance", "#3B82F6"),
            ("6", "Subjects", "#F59E0B")
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

            number = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            )

            number.pack(
                pady=(28, 5)
            )

            text = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            )

            text.pack()

        # ==================================
        # MAIN CONTENT
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
        # CLASS OVERVIEW
        # ==================================
        overview_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        overview_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        overview_title = ctk.CTkLabel(
            overview_frame,
            text="Class Overview",
            font=("Segoe UI", 26, "bold")
        )

        overview_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        overview_items = [
            "✓ 42 students enrolled",
            "✓ Attendance improved by 4%",
            "✓ Quiz performance increased",
            "⚠ 3 students require intervention",
            "✓ Homework completion at 89%",
            "✓ Midterm average: 78%"
        ]

        for item in overview_items:

            label = ctk.CTkLabel(
                overview_frame,
                text=item,
                font=("Segoe UI", 17),
                text_color="#CBD5E1"
            )

            label.pack(
                anchor="w",
                padx=25,
                pady=8
            )

        # ==================================
        # CLASS INFO PANEL
        # ==================================
        info_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        info_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        info_title = ctk.CTkLabel(
            info_frame,
            text="Class Information",
            font=("Segoe UI", 26, "bold")
        )

        info_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        info_items = [
            ("Class", "Grade 12A"),
            ("Homeroom", "Teacher A"),
            ("Students", "42"),
            ("Subjects", "6"),
            ("Semester", "Semester 1"),
            ("Risk Students", "3")
        ]

        for key, value in info_items:

            row = ctk.CTkFrame(
                info_frame,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=25,
                pady=8
            )

            left = ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            )

            left.pack(side="left")

            right = ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI", 16, "bold")
            )

            right.pack(side="right")