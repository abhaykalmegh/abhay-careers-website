from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
'certifi==2022.12.7',
'charset-normalizer==2.1.1',
'click==8.1.3',
'colorama==0.4.6',
'Flask==2.2.2',
'idna==3.4',
'importlib-metadata==5.2.0',
'itsdangerous==2.1.2',
'Jinja2==3.1.2',
'MarkupSafe==2.1.1',
'requests==2.28.1',
'urllib3==1.26.13',
'Werkzeug==2.2.2',
'zipp==3.11.0',
'gunicorn==20.1.0'
    ],
)