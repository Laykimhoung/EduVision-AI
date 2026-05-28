import customtkinter as ctk
from reports.student_pdf_generator import export_student_pdf


class StudentDetailPage(ctk.CTkFrame):

    def __init__(
            self,
            parent,
            student_data,
            back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.student_data = student_data
        self.back_command = back_command

        self.build_ui()

    # ==================================
    # EXPORT PDF
    # ==================================
    def export_pdf(self):

        export_student_pdf(
            self.student_data
        )

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        student = self.student_data

        # ==================================
        # MAIN SCROLL PAGE
        # ==================================
        scroll_page = ctk.CTkScrollableFrame(
            self,
            fg_color="#071224"
        )

        scroll_page.pack(
            fill="both",
            expand=True
        )

        # ==================================
        # HEADER
        # ==================================
        top_bar = ctk.CTkFrame(
            scroll_page,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=(25, 10)
        )

        # LEFT
        title_frame = ctk.CTkFrame(
            top_bar,
            fg_color="transparent"
        )

        title_frame.pack(side="left")

        title = ctk.CTkLabel(
            title_frame,
            text="Student Profile",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Monitor academic performance and risk prediction",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(anchor="w")

        # RIGHT BUTTONS
        btn_frame = ctk.CTkFrame(
            top_bar,
            fg_color="transparent"
        )

        btn_frame.pack(side="right")

        export_btn = ctk.CTkButton(
            btn_frame,
            text="Export PDF",
            width=150,
            height=46,
            corner_radius=16,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 16, "bold"),
            command=self.export_pdf
        )

        export_btn.pack(
            side="left",
            padx=(0, 12)
        )

        back_btn = ctk.CTkButton(
            btn_frame,
            text="← Back",
            width=140,
            height=46,
            corner_radius=16,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 16, "bold"),
            command=self.back_command
        )

        back_btn.pack(side="left")

        # ==================================
        # BODY
        # ==================================
        body = ctk.CTkFrame(
            scroll_page,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 35)
        )

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)

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

        # STUDENT NAME
        student_name = ctk.CTkLabel(
            left_panel,
            text=student["name"],
            font=("Segoe UI", 34, "bold")
        )

        student_name.pack(
            anchor="w",
            padx=25,
            pady=(25, 5)
        )

        meta = ctk.CTkLabel(
            left_panel,
            text=(
                f'ID: {student["id"]} • '
                f'{student["class"]} • '
                f'Semester {student["semester"]}'
            ),
            font=("Segoe UI", 16),
            text_color="#94A3B8"
        )

        meta.pack(
            anchor="w",
            padx=25
        )

        # ==================================
        # ATTENDANCE
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

        ctk.CTkLabel(
            attendance_card,
            text="Attendance",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        attendance = student["attendance"]

        if attendance < 60:
            attendance_color = "#EF4444"
        elif attendance < 75:
            attendance_color = "#F59E0B"
        else:
            attendance_color = "#10B981"

        ctk.CTkLabel(
            attendance_card,
            text=f"{attendance}%",
            font=("Segoe UI", 36, "bold"),
            text_color=attendance_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        # ==================================
        # PERFORMANCE
        # ==================================
        ctk.CTkLabel(
            left_panel,
            text="Academic Performance",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(5, 15)
        )

        academic_data = [
            ("Quiz", student["quiz"]),
            ("Homework", student["homework"]),
            ("Assignment", student["assignment"]),
            ("Midterm", student["midterm"]),
            ("Final", student["final"]),
            ("Participation", student["participation"]),
            ("Project", student["project"]),
            ("Behavior", student["behavior"])
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

            ctk.CTkLabel(
                row,
                text=key,
                font=("Segoe UI", 16)
            ).pack(
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

            ctk.CTkLabel(
                row,
                text=str(value),
                font=("Segoe UI", 16, "bold"),
                text_color=color
            ).pack(
                side="right",
                padx=20
            )

        # extra bottom spacing
        ctk.CTkFrame(
            left_panel,
            fg_color="transparent",
            height=20
        ).pack()

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

        ctk.CTkLabel(
            right_panel,
            text="AI Risk Prediction",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        risk_card = ctk.CTkFrame(
            right_panel,
            fg_color="#111827",
            corner_radius=22
        )

        risk_card.pack(
            fill="x",
            padx=25
        )

        risk = student["risk"]

        if risk == "High":
            risk_color = "#EF4444"
        elif risk == "Medium":
            risk_color = "#F59E0B"
        else:
            risk_color = "#10B981"

        ctk.CTkLabel(
            risk_card,
            text=f"{risk.upper()} RISK",
            font=("Segoe UI", 30, "bold"),
            text_color=risk_color
        ).pack(
            pady=25
        )

        ctk.CTkLabel(
            right_panel,
            text="Risk Factors",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(30, 15)
        )

        for factor in student["risk_factors"]:

            ctk.CTkLabel(
                right_panel,
                text=factor,
                font=("Segoe UI", 16),
                text_color="#CBD5E1"
            ).pack(
                anchor="w",
                padx=25,
                pady=6
            )

        recommendation_card = ctk.CTkFrame(
            right_panel,
            fg_color="#111827",
            corner_radius=22
        )

        recommendation_card.pack(
            fill="x",
            padx=25,
            pady=(30, 30)
        )

        ctk.CTkLabel(
            recommendation_card,
            text="Recommendation",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(
            recommendation_card,
            text=student["recommendation"],
            justify="left",
            font=("Segoe UI", 15),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )