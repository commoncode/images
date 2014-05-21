from setuptools import setup, find_packages

setup( name='images',
    version = '0.0.1',
    description = 'Images for Entropy Based Django Applications',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/images',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links = [
        'http://github.com/commoncode/entropy/tarball/master#egg=django-entropy-0.0.3',
    ],
    setup_requires = [
        'pip',
    ],
    install_requires = [
        'django-filepicker'
    ]
)
