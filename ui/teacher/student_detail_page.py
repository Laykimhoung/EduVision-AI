import customtkinter as ctk


class StudentDetailPage(ctk.CTkFrame):

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
            text="Student Profile",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Monitor academic performance and risk prediction",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=35
        )

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
            pady=25
        )

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # ==================================
        # LEFT PANEL
        # ==================================
        left_panel = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        left_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        # Student name
        student_name = ctk.CTkLabel(
            left_panel,
            text="Dara",
            font=("Segoe UI", 34, "bold")
        )

        student_name.pack(
            anchor="w",
            padx=25,
            pady=(25, 5)
        )

        student_meta = ctk.CTkLabel(
            left_panel,
            text="ID: 001 • Grade 12A • Semester 1",
            font=("Segoe UI", 16),
            text_color="#94A3B8"
        )

        student_meta.pack(
            anchor="w",
            padx=25
        )

        # ==================================
        # ATTENDANCE CARD
        # ==================================
        attendance_card = ctk.CTkFrame(
            left_panel,
            fg_color="#111827",
            corner_radius=22
        )

        attendance_card.pack(
            fill="x",
            padx=25,
            pady=25
        )

        attendance_title = ctk.CTkLabel(
            attendance_card,
            text="Attendance",
            font=("Segoe UI", 22, "bold")
        )

        attendance_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        attendance_value = ctk.CTkLabel(
            attendance_card,
            text="92%",
            font=("Segoe UI", 36, "bold"),
            text_color="#10B981"
        )

        attendance_value.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        # ==================================
        # ACADEMIC PERFORMANCE
        # ==================================
        section_title = ctk.CTkLabel(
            left_panel,
            text="Academic Performance",
            font=("Segoe UI", 26, "bold")
        )

        section_title.pack(
            anchor="w",
            padx=25,
            pady=(10, 20)
        )

        academic_data = [
            ("Quiz", 84),
            ("Homework", 81),
            ("Assignment", 78),
            ("Midterm", 75),
            ("Final", 89),
            ("Participation", 85),
            ("Project", 90),
            ("Behavior", 88)
        ]

        for key, value in academic_data:

            row = ctk.CTkFrame(
                left_panel,
                fg_color="#111827",
                corner_radius=18
            )

            row.pack(
                fill="x",
                padx=25,
                pady=6
            )

            left = ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI", 16)
            )

            left.pack(
                side="left",
                padx=20,
                pady=16
            )

            if value < 60:
                color = "#EF4444"
            elif value < 75:
                color = "#F59E0B"
            else:
                color = "#10B981"

            right = ctk.CTkLabel(
                row,
                text=str(value),
                font=("Segoe UI", 16, "bold"),
                text_color=color
            )

            right.pack(
                side="right",
                padx=20
            )

        # ==================================
        # RIGHT PANEL
        # ==================================
        right_panel = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        right_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # ==================================
        # RISK SCORE
        # ==================================
        risk_title = ctk.CTkLabel(
            right_panel,
            text="AI Risk Prediction",
            font=("Segoe UI", 26, "bold")
        )

        risk_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        risk_score_card = ctk.CTkFrame(
            right_panel,
            fg_color="#111827",
            corner_radius=22
        )

        risk_score_card.pack(
            fill="x",
            padx=25
        )

        risk_score_title = ctk.CTkLabel(
            risk_score_card,
            text="Risk Level",
            font=("Segoe UI", 18)
        )

        risk_score_title.pack(
            pady=(20, 5)
        )

        risk_score = ctk.CTkLabel(
            risk_score_card,
            text="LOW RISK",
            font=("Segoe UI", 30, "bold"),
            text_color="#10B981"
        )

        risk_score.pack(
            pady=(0, 20)
        )

        # ==================================
        # RISK FACTORS
        # ==================================
        factor_title = ctk.CTkLabel(
            right_panel,
            text="Risk Factors",
            font=("Segoe UI", 22, "bold")
        )

        factor_title.pack(
            anchor="w",
            padx=25,
            pady=(30, 15)
        )

        factors = [
            "✓ Strong attendance consistency",
            "✓ High final performance",
            "⚠ Midterm slightly declining",
            "✓ Homework submission stable"
        ]

        for factor in factors:

            lbl = ctk.CTkLabel(
                right_panel,
                text=factor,
                font=("Segoe UI", 15),
                text_color="#CBD5E1",
                justify="left"
            )

            lbl.pack(
                anchor="w",
                padx=25,
                pady=6
            )

        # ==================================
        # INTERVENTION
        # ==================================
        intervention = ctk.CTkFrame(
            right_panel,
            fg_color="#111827",
            corner_radius=22
        )

        intervention.pack(
            fill="x",
            padx=25,
            pady=30
        )

        intervention_title = ctk.CTkLabel(
            intervention,
            text="Recommendation",
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
                "Continue monitoring progress.\n"
                "Maintain attendance and\n"
                "encourage classroom participation."
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