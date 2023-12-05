from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://your.project.url',
    install_requires=[
        # List your project dependencies here.
        # For example:
        # 'numpy',
        # 'requests',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            # If you want to create command-line scripts, define them here
            # For example:
            # 'script_name = your_package.module:function',
        ],
    },
)
