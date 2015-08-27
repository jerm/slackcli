from setuptools import setup, find_packages

setup(
    name='slackcli',
    version='1.0.0',
    description='Slack CLI Application',
    url='https://github.com/traveloka/slackcli',
    author='Ricky Winata',
    author_email='ricky.w12@gmail.com',
    license='MIT',
    keywords='slack cli',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Topic :: System :: System Administration',
        'Topic :: Utilities',
    ],
    install_requires=['slackclient'],
    py_modules=['slackcli'],
    entry_points={
        'console_scripts': [
            'slackcli=slackcli:main',
        ],
    },
) 

