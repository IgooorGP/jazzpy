"""
Setup module to build distribution packages of jazzpy.
"""
from setuptools import setup

setup(
    name="jazzpy",
    version="0.1",
    url="https://github.com/IgooorGP/jazzpy",
    author="Igor Grillo Peternella",
    author_email="igor.feq@gmail.com",
    description="Python recreation of the first stage of the Jazz Jackrabbit game developed py Epic Megagames (1994).",
    packages=[
        "jazzpy",
        "jazzpy.camera",
        "jazzpy.levels",
        "jazzpy.sprites",
        "jazzpy.music",
        "jazzpy.scenes",
        "jazzpy.sprites",
    ],
    long_description=open("README.md").read(),
    zip_safe=False,
)
