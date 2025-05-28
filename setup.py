from setuptools import find_packages, setup 

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Joel AJ.',
    author_email= 'joelalexjohn9@gmail.com',
    install_requires = ["langchain","os","langchain_google_genai","streamlit","PyPDF2"]
    packages = find_packages()
)