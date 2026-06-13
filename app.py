import json
from src.resume_builder import build_resume


def main():
    #Main function to run the Resume Parser.

    # Resume file path
    pdf_path = "resumes/test_resume.pdf"

    # Build structured resume
    resume = build_resume(pdf_path)

    # Print structured resume
    print("\n===== Structured Resume =====\n")
    print(json.dumps(resume, indent=4))

    # Save output as JSON
    with open("outputs/resume.json", "w") as file:
        json.dump(
            resume,
            file,
            indent=4
        )

    print("\n Resume saved successfully!")


# Run application
if __name__ == "__main__":
    main()