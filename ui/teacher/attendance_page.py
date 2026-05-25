import customtkinter as ctk


class AttendancePage(ctk.CTkFrame):

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
            text="Attendance",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Track attendance and identify at-risk students",
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

        date_label = ctk.CTkLabel(
            top_bar,
            text="Today: 26 May 2026",
            font=("Segoe UI", 16),
            text_color="#CBD5E1"
        )

        date_label.pack(side="right")

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
            ("38", "Present", "#10B981"),
            ("3", "Absent", "#EF4444"),
            ("1", "Late", "#F59E0B"),
            ("91%", "Attendance", "#3B82F6")
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
            text="Attendance List",
            font=("Segoe UI", 26, "bold")
        )

        table_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        # Header
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
            ("Status", 140),
            ("Attendance %", 140),
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

        # Scrollable rows
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
            ("001", "Dara", "Present", "95%"),
            ("002", "Sokha", "Absent", "58%"),
            ("003", "Lina", "Late", "80%"),
            ("004", "Nita", "Present", "92%"),
            ("005", "Visal", "Absent", "61%"),
            ("006", "Kimlong", "Present", "94%"),
            ("007", "Sophy", "Late", "82%")
        ]

        for sid, name, status, rate in students:

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

            if status == "Present":
                status_color = "#10B981"
            elif status == "Late":
                status_color = "#F59E0B"
            else:
                status_color = "#EF4444"

            values = [
                (sid, 80),
                (name, 180),
                (status, 140),
                (rate, 140)
            ]

            for value, width in values:

                lbl = ctk.CTkLabel(
                    row,
                    text=value,
                    width=width,
                    font=("Segoe UI", 15),
                    text_color=(
                        status_color
                        if value == status
                        else "#E5E7EB"
                    )
                )

                lbl.pack(
                    side="left",
                    padx=5,
                    pady=18
                )

            edit_btn = ctk.CTkButton(
                row,
                text="Edit",
                width=100,
                height=38,
                corner_radius=12,
                fg_color="#EF4444",
                hover_color="#DC2626"
            )

            edit_btn.pack(
                side="left",
                padx=8
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
            text="Attendance Risk",
            font=("Segoe UI", 26, "bold")
        )

        risk_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        risks = [
            ("Sokha", "58%", "High Risk"),
            ("Visal", "61%", "Medium Risk"),
            ("Lina", "80%", "Low Risk")
        ]

        for name, rate, risk in risks:

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

            top = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            top.pack(
                fill="x",
                padx=18,
                pady=(18, 8)
            )

            student_name = ctk.CTkLabel(
                top,
                text=name,
                font=("Segoe UI", 17, "bold")
            )
            student_name.pack(side="left")

            attendance = ctk.CTkLabel(
                top,
                text=rate,
                font=("Segoe UI", 15),
                text_color="#94A3B8"
            )
            attendance.pack(side="right")

            if "High" in risk:
                risk_color = "#EF4444"
            elif "Medium" in risk:
                risk_color = "#F59E0B"
            else:
                risk_color = "#10B981"

            risk_label = ctk.CTkLabel(
                card,
                text=risk,
                font=("Segoe UI", 15, "bold"),
                text_color=risk_color
            )

            risk_label.pack(
                anchor="w",
                padx=18,
                pady=(0, 18)
            )