from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pymuco",
    packages=find_packages(),
    version="1.1.6",
    description="A Python Music Computation Library",
    author="German Margon",
    author_email="gmargon@pymuco.org",
    url="https://pymuco.org/",
    license="BSD-3-Clause",
    install_requires=[
        "numpy>=1.19.0",
        "midiutil>=1.2.1",
        "sounddevice>=0.4.5",
        "scipy>=1.7.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
