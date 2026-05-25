import customtkinter as ctk


class AnalyticsPage(ctk.CTkFrame):

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
            text="Analytics & Risk Prediction",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Analyze student performance and identify intervention needs",
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

        risk_filter = ctk.CTkComboBox(
            top_bar,
            values=[
                "All Risk",
                "High Risk",
                "Medium Risk",
                "Low Risk"
            ],
            width=180,
            height=46,
            corner_radius=14,
            button_color="#EF4444",
            button_hover_color="#DC2626"
        )

        risk_filter.set("All Risk")
        risk_filter.pack(side="right")

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
            ("42", "Students", "#3B82F6"),
            ("4", "High Risk", "#EF4444"),
            ("7", "Medium Risk", "#F59E0B"),
            ("31", "Low Risk", "#10B981")
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

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # ==================================
        # RISK TABLE
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
            text="Student Risk Prediction",
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
            ("Attend.", 90),
            ("Quiz", 70),
            ("Midterm", 90),
            ("Final", 70),
            ("Risk", 100)
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
        # SCROLL TABLE
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
            ("Sokha", "58%", 54, 60, 57, "High"),
            ("Kimlong", "61%", 55, 58, 60, "High"),
            ("Visal", "74%", 68, 66, 70, "Medium"),
            ("Lina", "83%", 79, 81, 84, "Low"),
            ("Dara", "95%", 84, 75, 89, "Low"),
            ("Nita", "92%", 91, 89, 94, "Low")
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
                (student[1], 90),
                (student[2], 70),
                (student[3], 90),
                (student[4], 70),
                (student[5], 100)
            ]

            for value, width in values:

                color = "#E5E7EB"

                if value == "High":
                    color = "#EF4444"
                elif value == "Medium":
                    color = "#F59E0B"
                elif value == "Low":
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
        # AI INSIGHTS PANEL
        # ==================================
        side_panel = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        side_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        insight_title = ctk.CTkLabel(
            side_panel,
            text="AI Insights",
            font=("Segoe UI", 26, "bold")
        )

        insight_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        insights = [
            "⚠ 4 students are high risk",
            "✓ Attendance strongly impacts risk",
            "⚠ Quiz trend declining in Grade 12A",
            "✓ Homework completion improving",
            "⚠ Sokha needs intervention"
        ]

        for item in insights:

            lbl = ctk.CTkLabel(
                side_panel,
                text=item,
                font=("Segoe UI", 16),
                text_color="#CBD5E1",
                justify="left"
            )

            lbl.pack(
                anchor="w",
                padx=25,
                pady=8
            )

        # ==================================
        # INTERVENTION PANEL
        # ==================================
        intervention = ctk.CTkFrame(
            side_panel,
            fg_color="#111827",
            corner_radius=20
        )

        intervention.pack(
            fill="x",
            padx=25,
            pady=25
        )

        intervention_title = ctk.CTkLabel(
            intervention,
            text="Recommended Action",
            font=("Segoe UI", 20, "bold")
        )

        intervention_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        intervention_text = ctk.CTkLabel(
            intervention,
            text=(
                "Schedule intervention for students\n"
                "with attendance below 65%\n"
                "and quiz average below 60."
            ),
            justify="left",
            font=("Segoe UI", 15),
            text_color="#CBD5E1"
        )

        intervention_text.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )