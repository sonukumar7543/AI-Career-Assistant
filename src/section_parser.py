from src.constants import SECTION_HEADINGS


def extract_sections(text):
    # Extract all major resume sections.

    sections = {}

    current_section = None

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Is this line a heading?
        if line.upper() in SECTION_HEADINGS:

            current_section = line.upper()

            sections[current_section] = []

        elif current_section:

            sections[current_section].append(line)

    return sections