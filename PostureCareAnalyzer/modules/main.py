import sys
from modules.posture_capture import run_camera
from modules.report_generator import generate_pdf_report

def main():
    run_camera()
    generate_pdf_report("output_report.pdf")

if __name__ == "__main__":
    main()
