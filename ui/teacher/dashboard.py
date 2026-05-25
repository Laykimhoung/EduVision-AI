from ui.components.dashboard_shell import DashboardShell
import customtkinter as ctk


class TeacherDashboard(DashboardShell):

    def __init__(self, parent):

        super().__init__(
            parent,
            role_name="Teacher",
            accent_color="#EF4444",
            menu_items=[
                "Dashboard",
                "Classroom",
                "Students",
                "Attendance",
                "Assessment",
                "Analytics"
            ]
        )

        self.navigate("Dashboard")

    # ==================================
    # NAVIGATION
    # ==================================
    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def navigate(self, page_name):

        self.clear_content()

        if page_name == "Dashboard":
            self.build_dashboard()

        elif page_name == "Classroom":
            from ui.teacher.classroom_page import ClassroomPage
            ClassroomPage(self.content).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Students":
            from ui.teacher.students_page import StudentsPage
            StudentsPage(self.content).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Attendance":
            from ui.teacher.attendance_page import AttendancePage
            AttendancePage(self.content).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Assessment":
            from ui.teacher.assessment_page import AssessmentPage
            AssessmentPage(self.content).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Analytics":
            from ui.teacher.analytics_page import AnalyticsPage
            AnalyticsPage(self.content).pack(
                fill="both",
                expand=True
            )

    # ==================================
    # DASHBOARD UI
    # ==================================
    def build_dashboard(self):

        # ===============================
        # HEADER
        # ===============================
        title = ctk.CTkLabel(
            self.content,
            text="Teacher Dashboard",
            font=("Segoe UI", 40, "bold")
        )
        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self.content,
            text="Monitor classes, attendance, assessment and student risk",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )
        subtitle.pack(
            anchor="w",
            padx=35
        )

        # ===============================
        # STATS CARDS
        # ===============================
        stats_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        stats_frame.pack(
            fill="x",
            padx=30,
            pady=30
        )

        stats = [
            ("240", "Students", "#EF4444"),
            ("92%", "Attendance", "#10B981"),
            ("12", "High Risk", "#F59E0B"),
            ("18", "Assignments", "#3B82F6")
        ]

        for value, label, color in stats:

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                height=150,
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
                pady=(30, 5)
            )

            txt = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 17),
                text_color="#94A3B8"
            )
            txt.pack()

        # ===============================
        # MAIN AREA
        # ===============================
        body = ctk.CTkFrame(
            self.content,
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

        # ===============================
        # RECENT ACTIVITY
        # ===============================
        activity_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        activity_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        activity_title = ctk.CTkLabel(
            activity_frame,
            text="Recent Activity",
            font=("Segoe UI", 26, "bold")
        )
        activity_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        activities = [
            "✓ Attendance recorded for Grade 12A",
            "✓ Quiz scores updated",
            "✓ Homework submitted by 34 students",
            "✓ Midterm grades published",
            "⚠ 4 students marked high risk"
        ]

        for item in activities:

            label = ctk.CTkLabel(
                activity_frame,
                text=item,
                font=("Segoe UI", 17),
                text_color="#CBD5E1"
            )
            label.pack(
                anchor="w",
                padx=25,
                pady=8
            )

        # ===============================
        # QUICK ACTIONS
        # ===============================
        action_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        action_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        quick_title = ctk.CTkLabel(
            action_frame,
            text="Quick Actions",
            font=("Segoe UI", 26, "bold")
        )
        quick_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        actions = [
            "Take Attendance",
            "Open Students",
            "Assessment",
            "Analytics"
        ]

        for action in actions:

            btn = ctk.CTkButton(
                action_frame,
                text=action,
                height=50,
                corner_radius=18,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold")
            )

            btn.pack(
                fill="x",
                padx=25,
                pady=8
            )