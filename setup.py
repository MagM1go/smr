import setuptools
import pathlib


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="utf8")

setuptools.setup(
	name="some_random_python",
	version="2.0",
	author="MagMigo",
	description="Simple wrapper for some-random-api.",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MagM1go/smr",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)
