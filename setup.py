from setuptools import setup, find_packages

setup(
    name='SimpleEmbed',
    version='v1', 
    packages=find_packages(),
    description='A utility for creating and sending Discord embeds',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ItsPyDevs',
    author_email='None',
    url='https://github.com/ItsPyDevs/SimpleEmbed',  # URL to your project
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)
