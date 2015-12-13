import setuptools

setuptools.setup(
    name='compy',
    version='0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'wxpython',
        'fuzzywuzzy',
        'unidecode',
    ],
)

