from setuptools import setup, find_packages

setup(
    name='talon',
    author='Chris Withers',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=['testfixtures', 'nose', 'nose-cov'],
        build=['sphinx', 'pkginfo', 'setuptools-git', 'twine']
    ),
    )
