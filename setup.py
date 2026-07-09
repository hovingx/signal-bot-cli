from setuptools import setup, find_packages

setup(
    name="signal-bot-cli",
    version="1.0.0",
    description="signal-bot.ai CLI — real-time trading signals & market data in your terminal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="signal-bot.ai",
    author_email="hello@signal-bot.ai",
    url="https://signal-bot.ai",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28",
        "tabulate>=0.9",
    ],
    extras_require={
        "dev": [
            "pytest>=7",
            "ruff>=0.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "signal-bot=signalbot.cli:main",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
)
