import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name="image_plot", # Replace with your own username
            version="0.0.1",
            author="Collin Brake",
            author_email="collin@bec-systems.com",
            description="A package to plot images as surfaces",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/collinbrake/image_plot",
            packages=setuptools.find_packages(),
            classifiers=[
                        "Programming Language :: Python :: 3",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: OS Independent",
                            ],
                python_requires='>=3.6',
    )
