from setuptools import setup, find_packages
from version import get_git_version
import os

def get_requirements():
    thelibFolder = os.path.dirname(os.path.realpath(__file__))
    requirementPath = thelibFolder + '/requirements.txt'
    if os.path.isfile(requirementPath):
        with open(requirementPath) as f:
            return f.read().splitlines()
    else:
        return []

setup(
    name='pyplot-3d',
    version=get_git_version(),    
    description='A Python library for drawing a 3D objects using Python Matplotlib library.',
    url='https://github.com/aniongithub/pyplot-3d',
    author='Ani Balasubramaniam, Kanishke Gamagedara',
    author_email='ani@anionline.me',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
