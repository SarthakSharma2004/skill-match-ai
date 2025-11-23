import os
from parsers.resume_parser import ResumeParser
from langchain_community import Documents


def test_pdf_parsing() :
    parser = ResumeParser()