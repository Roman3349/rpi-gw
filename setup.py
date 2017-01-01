from setuptools import setup

with open("README.md") as stream:
    long_description = stream.read()

setup(
    name="rpigw",
    description="Python Raspberry Pi GSM and IQRF gateway.",
    version="0.0.1",
    author="Roman Ondráček",
    author_email="ondracek.roman@centrum.cz",
    url="https://github.com/Roman3349/rpi-gw",
    package_dir={"": "src"},
    packages=[
        "rpigw",
        "rpigw.gsm",
        "rpigw.iqrf",
        "rpigw.util"
    ],
    license="GPL v3",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
    ],
    install_requires=[
        "pyserial >= 3.1.1"#,
#        "pylibiqrf >= 0.0.1"
    ]
)

