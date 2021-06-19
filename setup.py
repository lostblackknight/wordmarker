from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='wordmarker',
    version='0.0.7',
    author='chensixiang',
    author_email='chensixiang1234@gmail.com',
    license_file='LICENSE',
    license='MIT',
    url='https://wordmarker.readthedocs.io',
    download_url='https://pypi.org/project/wordmarker/',
    project_urls={
        "Code": "https://github.com/lostblackknight/wordmarker",
        "Issue tracker": "https://github.com/lostblackknight/wordmarker/issues",
    },
    description='Word documentation generator',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    packages=find_packages(
        exclude=['tests', 'tests.contexts', 'tests.templates', 'tests.utils'],
    ),
    zip_safe=False,
    install_requires=[
        'chardet==4.0.0',
        'coloredlogs==15.0',
        'greenlet==1.0.0',
        'humanfriendly==9.1',
        'numpy==1.19.2',
        'pandas>=1.2.3',
        'psycopg2==2.8.6',
        'pyreadline==2.1',
        'python-dateutil==2.8.1',
        'pytz==2021.1',
        'PyYAML==5.4.1',
        'six==1.15.0',
        'SQLAlchemy==1.4.5',
        'click==7.1.2',
        'ruamel.yaml==0.16.12',
        'ruamel.yaml.clib==0.2.2',
        'docutils>=0.13.1',
        'Pygments>=2.5.1',
        'bleach==3.3.0',
        'docxtpl==0.11.4',
        'Jinja2==2.11.3',
        'lxml==4.6.3',
        'MarkupSafe==1.1.1',
        'python-docx==0.8.10',
    ],
    entry_points={
        'console_scripts': [
            'wordmarker-quickstart = wordmarker.scripts.quickstart:main',
        ],
    },
    python_requires=">=3.7",
)
