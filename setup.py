from setuptools import setup
setup(
    name="md-toc",
    py_modules=["md_toc"],
    packages=[],
    entry_points={
        'console_scripts': ["toc=md_toc:main"],
        },
    author="Olav Vahtras",
    author_email="vahtras@kth.se",
    description="",
    )
 
