from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.31"
DESCRIPTION = "Automating video and short content creation with AI"
LONG_DESCRIPTION = "A powerful tool for automating content creation. It simplifies video creation, footage sourcing, voiceover synthesis, and editing tasks."


setup(
    name="shortgpt",
    version=VERSION,
    author="RayVentura",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    package_data={
        "": ["*.yaml", "*.json"]
    },  # This will include all yaml files in package
    install_requires=[
        "ffmpeg",
        "ffmpeg-python",
        "python-dotenv",
        "openai",
        "tiktoken",
        "tinydb",
        "tinymongo",
        "proglog",
        "yt-dlp",
        "torch",
        "whisper-timestamped",
        "torchaudio",
        "pillow",
        "protobuf",
        "edge-tts",
        "moviepy @ https://github.com/deepInTheData/moviepy/archive/v25.12.2023.zip",
        "progress",
        "questionary",
    ],
    keywords=[
        "python",
        "video",
        "content creation",
        "AI",
        "automation",
        "editing",
        "voiceover synthesis",
        "video captions",
        "asset sourcing",
        "tinyDB",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
