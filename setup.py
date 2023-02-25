from setuptools import setup, find_packages

setup(
    name='personal_assistant',
    version='1.0.0',
    description='Package with scripts for using Personal assistant bot',
    long_description=open('README.md').read(),
    url='https://github.com/Serhii-Olkhovskyi/personal_assistant',
    author1='ProPy10_team',
    readme="README.md",
    license="LICENSE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['prettytable', 'pyfiglet', 'tabulate'],
    packages=find_packages(),
    entry_points={'console_scripts': ["PersonalAssistant=personal_assistant.main:main"]}

    # PersonalAssistant - command that shall be executed in the terminal
    # after "=" - the path to the file where the function is located -> personal_assistant.main
    # after ":" - the function that shall be performed -> main
)
