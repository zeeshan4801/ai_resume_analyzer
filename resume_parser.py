import pymupdf
from docx import Document


def extract_text_from_file(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return extract_docx(uploaded_file)

    else:
        raise ValueError("Unsupported file format")


def extract_pdf(file):

    text = ""

    pdf = pymupdf.open(
        stream=file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text


def extract_docx(file):

    doc = Document(file)

    return "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )
