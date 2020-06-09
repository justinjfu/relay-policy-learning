from distutils.core import setup
from setuptools import find_packages

setup(
    name='adept_envs',
    version='0.1',
    #package_data={
    #  'adept_envs': ['adept_envs/adept_envs/franka/assets/*.xml'],
    #},
    #include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['gym', 
                      'numpy', 
                      'mujoco_py', 
                      'click', 
                      'dm_control @ git+git://github.com/deepmind/dm_control@master#egg=dm_control',
                      'mjrl @ git+git://github.com/aravindr93/mjrl@master#egg=mjrl'],
    packages=find_packages(),
)

