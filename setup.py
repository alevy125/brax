# Copyright 2022 The Brax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""setup.py for Brax.

Install for development:

  pip intall -e .
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name="brax",
    version="0.0.15",
    description=("A differentiable physics engine written in JAX."),
    author="Brax Authors",
    author_email="no-reply@google.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/google/brax",
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    scripts=["bin/learn"],
    install_requires=[
        "absl-py>=1.3.0, <1.4.0",
        "dataclasses",
        "dm_env",
        "flax>=0.6.3, <0.6.4",
        "gym",
        "grpcio>=1.51.1,<1.51.2",
        "jax>=0.4.1, <0.4.2",
        "jaxlib>=0.4.1, <0.4.2",
        "numpy>=1.24.1, <1.24.2",
        "optax>=0.1.4, <0.1.5",
        "Pillow>=9.4.0, <9.5.0",
        "pytinyrenderer>=0.0.13, <0.0.14",
        "tensorboardX>=2.5.1, <2.6",
        "trimesh>=3.17.1, <3.18.0",
        "typing-extensions>=4.4.0, <4.5.0",
        # TODO: remove when
        #   https://github.com/google/flax/issues/2190 is fixed.
        "PyYAML>=6.0",
    ],
    extras_require={
        "develop": ["pytest", "transforms3d"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="JAX reinforcement learning rigidbody physics",
    data_files=[
        ("testdata", ["brax/tests/testdata/cylinder.stl"])
    ],
)
