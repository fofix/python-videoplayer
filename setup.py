#!/usr/bin/env python


from distutils.command.clean import clean as Clean
try:
    from skbuild import setup
except ImportError:
    from setuptools import setup
import os


class CleanCommand(Clean):
    """ Remove generated files """

    def run(self):
        Clean.run(self)

        # remove build_ext inplace generated files
        for dirpath, dirnames, filenames in os.walk('videoplayer'):
            for filename in filenames:
                extension = os.path.splitext(filename)[1]
                # bin
                if extension in (".so", ".dll", ".pyc"):
                    print("Remove", filename)
                    os.unlink(os.path.join(dirpath, filename))
                    continue

                # libs
                if extension in ('.c', '.h'):
                    pyx_file = str.replace(filename, extension, '.pyx')
                    if os.path.exists(os.path.join(dirpath, pyx_file)):
                        print("Remove", filename)
                        os.unlink(os.path.join(dirpath, filename))


# Readme
readme_filepath = os.path.join(os.path.dirname(__file__), "README.md")
try:
    import pypandoc
    long_description = pypandoc.convert(readme_filepath, 'rst')
except ImportError:
    long_description = open(readme_filepath).read()

# setup
setup(
    name='videoplayer',
    version='1.1.dev0',
    description='VideoPlayer is a C-extension in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='FoFiX team',
    author_email='fofix@perdu.fr',
    license='GPLv2+',
    url='https://github.com/fofix/python-videoplayer',
    packages=['videoplayer'],
    package_data={'videoplayer': ['*.dll']},
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='ogg',
    #ext_modules=cythonize(ext, compiler_directives={'language_level': sys.version_info[0]}),
    #setup_requires=['cython', 'pytest-runner', 'cmake'],
    setup_requires=['pytest-runner', 'cmake'],
    #install_requires=[
    #    'Cython >= 0.27',
    #],
    test_suite="tests",
    tests_require=['pytest'],
    extras_require={
        'tests': ['pytest'],
    },
    cmdclass={
        'clean': CleanCommand,
    },
)
