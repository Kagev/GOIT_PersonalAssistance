from setuptools import setup, find_namespace_packages

setup(
    name='Willy',
    version='v0.9.3',
    description='Твій особистий помічник',
    url='https://github.com/Kagev/GOIT_PersonalAssistance',
    author='PyCrafters',
    author_email='PyCrafters@goit.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'willy': ['willy = project_willy.main']}
)