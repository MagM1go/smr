import setuptools


setuptools.setup(
	name="smr-py",
	version="1.0.0",
	author="Eric Chi",
	description="Simple wrapper for some-random-api on python.",
	url="https://github.com/MagM1go/smr",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)