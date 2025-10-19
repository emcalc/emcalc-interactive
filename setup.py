from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='emcalc',
    version='12.0.0',
    python_requires=">=3.8,<4",
    author='eymndev',
    author_email='eymenyildirim13@icloud.com',
    description='Calculates E=mc^2, auto-converts gram to kilogram and returns energy in joules.',
    url='https://emcalc.github.io//',
    license='GNU Public License v3.0',
    install_requires=requirements,
    py_modules=[
        'emcalc'
    ],
)
