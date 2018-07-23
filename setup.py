from setuptools import setup

setup(
    name='eol_finesse_library',
    version='0.0.4',
    packages=['eol_finesse_library'],
    url='https://github.com/mikelovskij/eol_finesse_library',
    license='MIT',
    author='Michele Valentini',
    author_email='michele.valentini@unitn.it',
    description=('some useful functions to generate .kat scripts for '
                 'the study of a triangular cavity matching.'),
    install_requires=["numpy"],
    python_requires='>=3.6'
)
