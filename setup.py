import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='ia256utilities',
                 version='0.4.2',
                 description='A set of useful utilities',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/IceArrow256/ia256utilities',
                 author='IceArrow256',
                 author_email='icearrow256@gmail.com',
                 license='The Unlicense',
                 packages=['ia256utilities'],
                 zip_safe=False)
