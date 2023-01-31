import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swifttools",
    version="0.1",
    author="Yannick Bahe",
    author_email="bahe@strw.leidenuniv.nl",
    description="Tools for analysing SWIFT simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="www.swiftsim.com",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: OS independent"
    ],
    python_requires='>=3.6'
)

