from setuptools import setup, find_packages
import os

version = '0.2'

setup(
    name='avrc.theme.leadtheway',
    version=version,
    description="Diazo theme for the Lead The Way Campaign",
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/avrc.theme.leadtheway',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['avrc', 'avrc.theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'five.grok',
        'plone.app.theming',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
