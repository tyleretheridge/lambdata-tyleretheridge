


from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-tyleretheridge", # the name that you will install via pip
    version="0.1",
    author="Tyler Etheridge",
    author_email="tylerjetheridge98@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)