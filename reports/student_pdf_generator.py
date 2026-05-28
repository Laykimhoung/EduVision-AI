from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Paragraph
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import pagesizes
from pathlib import Path
from datetime import datetime


def export_student_pdf(student):

    # ==================================
    # SAVE LOCATION
    # ==================================
    downloads_path = Path.home() / "Downloads"

    file_name = (
        f'{student["name"].replace(" ", "_")}'
        f'_report.pdf'
    )

    file_path = downloads_path / file_name

    # ==================================
    # PDF DOCUMENT
    # ==================================
    doc = SimpleDocTemplate(
        str(file_path),
        pagesize=pagesizes.A4,
        topMargin=35,
        bottomMargin=35,
        leftMargin=35,
        rightMargin=35
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    # ==================================
    # HEADER
    # ==================================
    story.append(
        Paragraph(
            "EduVision AI",
            title_style
        )
    )

    story.append(
        Paragraph(
            f'Student Performance Report - {student["name"]}',
            heading_style
        )
    )

    story.append(
        Paragraph(
            f'Generated on: '
            f'{datetime.now().strftime("%d/%m/%Y")}',
            body_style
        )
    )

    story.append(Spacer(1, 20))

    # ==================================
    # STUDENT INFO
    # ==================================
    story.append(
        Paragraph(
            "Student Information",
            heading_style
        )
    )

    info_data = [
        ["Student", student["name"]],
        ["ID", student["id"]],
        ["Class", student["class"]],
        ["Semester", "Semester 1"],
        ["Attendance", f'{student["attendance"]}%'],
        ["Risk", student["risk"]]
    ]

    info_table = Table(
        info_data,
        colWidths=[150, 250]
    )

    info_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (0, -1),
         colors.white),

        ("BACKGROUND", (1, 0), (1, -1),
         colors.HexColor("#F8FAFC")),

        ("FONTNAME", (0, 0), (-1, -1),
         "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER"),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE")
    ]))

    story.append(info_table)

    story.append(Spacer(1, 25))

    # ==================================
    # PERFORMANCE TABLE
    # ==================================
    story.append(
        Paragraph(
            "Academic Performance",
            heading_style
        )
    )

    performance_data = [
        ["Category", "Score"],
        ["Quiz", student["quiz"]],
        ["Homework", student["homework"]],
        ["Assignment", student["assignment"]],
        ["Midterm", student["midterm"]],
        ["Final", student["final"]],
        ["Participation", student["participation"]],
        ["Project", student["project"]],
        ["Behavior", student["behavior"]]
    ]

    performance_table = Table(
        performance_data,
        colWidths=[220, 180]
    )

    performance_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (-1, 0),
         colors.white),

        ("FONTNAME", (0, 0), (-1, 0),
         "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER"),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE")
    ]))

    story.append(performance_table)

    story.append(Spacer(1, 25))

    # ==================================
    # AI RISK ANALYSIS
    # ==================================
    story.append(
        Paragraph(
            "AI Risk Prediction",
            heading_style
        )
    )

    risk_color = "#DCFCE7"

    if student["risk"] == "Medium":
        risk_color = "#FEF3C7"

    elif student["risk"] == "High":
        risk_color = "#FEE2E2"

    risk_table = Table([
        ["Risk Level", student["risk"]]
    ], colWidths=[200, 200])

    risk_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (0, 0),
         colors.white),

        ("BACKGROUND", (1, 0), (1, 0),
         colors.HexColor(risk_color)),

        ("FONTNAME", (0, 0), (-1, -1),
         "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER")
    ]))

    story.append(risk_table)

    story.append(Spacer(1, 25))

    # ==================================
    # RECOMMENDATION
    # ==================================
    story.append(
        Paragraph(
            "Recommendation",
            heading_style
        )
    )

    if student["risk"] == "High":

        recommendation = (
            "Immediate intervention recommended. "
            "Monitor attendance and provide "
            "additional academic support."
        )

    elif student["risk"] == "Medium":

        recommendation = (
            "Continue monitoring progress and "
            "encourage participation improvement."
        )

    else:

        recommendation = (
            "Maintain current academic performance "
            "and attendance consistency."
        )

    story.append(
        Paragraph(
            recommendation,
            body_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by EduVision AI",
            body_style
        )
    )

    # ==================================
    # BUILD PDF
    # ==================================
    doc.build(story)

    print(
        f"Student PDF exported: {file_path}"
    )

    return str(file_path)