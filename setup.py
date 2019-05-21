from setuptools import setup, find_packages

# function bodies left out for presentation - 16 LoC
check_env()
copy_overlays()
copy_notebooks()

setup(
    name="pynq-helloworld",
    version='1.0',
    install_requires=['pynq>=2.3'],
    packages=find_packages(),
    package_data={
        '': hw_data_files,
    },
    description="PYNQ example designs supporting PYNQ-enabled boards"
)
