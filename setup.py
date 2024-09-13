from setuptools import setup, find_packages

setup(
    name='PlotMagic',
    version='0.3',
    description='A Python package for easy-to-use advanced visualizations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aditya Srivastav',
    author_email='adityathestar2006@gmail.com',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'numpy',
        'pandas',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
