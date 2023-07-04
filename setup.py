from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pymuco",
    packages=["pymuco"],
    version="1.0.0",
    description="A Python Music Computation Library",
    author="German Margon",
    author_email="gmargon@pymuco.org",
    url="https://pymuco.org/",
    license="BSD-3-Clause",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
