from setuptools import setup, find_packages

setup(
    name='wordmarker',
    version='0.0.1',
    author='chensixiang',
    author_email='chensixiang1234@gmail.com',
    license_file='LICENSE',
    license='MIT',
    download_url='https://pypi.org/project/wordmarker/',
    project_urls={
        "Code": "https://github.com/lostblackknight/wordmarker",
        "Issue tracker": "https://github.com/lostblackknight/wordmarker/issues",
    },
    description='Word documentation generator',
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
        'pywin32==227',
        'PyYAML==5.4.1',
        'six==1.15.0',
        'SQLAlchemy==1.4.5',
        'click==7.1.2',
        'ruamel.yaml==0.16.12',
        'ruamel.yaml.clib==0.2.2',
        'docutils>=0.13.1',
        'Pygments>=2.5.1',
        'bleach==3.3.0',
    ],
    entry_points={
        'console_scripts': [
            'wordmarker-quickstart = wordmarker.scripts.quickstart:main',
        ],
    },
    python_requires=">=3.7",
)
