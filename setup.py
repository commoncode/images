from setuptools import setup, find_packages


setup(
    name='images',
    version='0.0.1',
    description='Images for Entropy Based Django Applications',
    author='Daryl Antony',
    author_email='daryl@commoncode.com.au',
    url='https://github.com/commoncode/images',
    keywords=['django'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    dependency_links=[
        'http://github.com/commoncode/entropy/tarball/master#egg=entropy',
    ],
    setup_requires=['pip'],
    install_requires=['pillow', 'django-filepicker']
)
