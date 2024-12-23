from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sundae_theme/__init__.py
from sundae_theme import __version__ as version

setup(
	name="sundae_theme",
	version=version,
	description="multi themes for frappe & erpnext apps",
	author="vikram kumar",
	author_email="vikram.kumar@softude.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
