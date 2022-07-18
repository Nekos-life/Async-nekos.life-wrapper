from setuptools import setup
from re import search, MULTILINE

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

readme = ""
with open("README.rst") as f:
    readme = f.read()

version = ""
with open("anekos/__init__.py") as f:
    version = search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), MULTILINE
    ).group(1)


setup(
    name="anekos",
    author="NiumXp",
    project_urls={
        "Website": "https://nekos.life",
        "Issue tracker": "https://github.com/Nekos-life/Async-nekos.life-wrapper",
    },
    version=version,
    packages=["anekos"],
    license="MIT",
    description="An unofficial asynchronous wrapper for nekos.life API",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
