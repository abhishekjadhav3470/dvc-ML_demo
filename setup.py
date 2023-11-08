from setuptools import setup

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.3",
    author="abhishekjadhav3470",
    description="A small package for dvc Ml pipeline",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url="https://github.com/abhishekjadhav3470/dvc-ML_demo.git",
    author_email="abhishekjadhav3470@gmail.com",
    packages=["src"],
    license="GNU",
    python_requires =">=3.7",
    install_requires=[
    "dvc",         
    "pandas",      
    "scikit-learn" 
]

)