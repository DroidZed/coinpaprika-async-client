from setuptools import setup

setup(
    name="coinpaprika_async",
    version="3.0.0rc2",
    author="DroidZed",
    author_email="droid.zed77@outlook.com",
    description="An asynchronous client for the coinpaprika API.",
    packages=["coinpaprika_async"],
    url="https://github.com/DroidZed/coinpaprika-async-client.git",
    license="MIT",
    install_requires=["httpx"],
    keywords="coinpaprika_async api cryptocurrency async httpx client",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
