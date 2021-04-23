from setuptools import setup, find_packages


def read(f):
    return open(f, encoding='utf-8').read()


setup(
    name='easy-nhl',
    version='0.3',
    description='Making it easier to use the NHL API in python projects.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/branks42/easy-nhl',
    author='Justin Branco',
    author_email='jbranco@nd.edu',
    license='MIT',
    packages=find_packages(include=['easy_nhl', 'easy_nhl.*']),  # Required,
    keywords=['hockey', 'NHL', 'api', 'statistics'],
    install_requires=[
        'requests>=2.25.1'
    ],
    zip_safe=False)
