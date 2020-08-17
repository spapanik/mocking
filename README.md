<p align="center">
<a href="https://github.com/spapanik/mocking/blob/master/LICENSE.txt"><img alt="License" src="https://img.shields.io/github/license/spapanik/mocking"></a>
<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# mocking: A showcase of different situations of mock.patch usage

## Installation and usage

The recommended way to install and use mocking is via _yam_, which can be installed by `pip install --user yamk`. Please make sure that you add the path where pip installs user-local binaries to you $PATH variable. Arch Linux users can install yam from AUR, as `python-yamk`. Also, _poetry_ (at least version 1.0.0) is required.

### Installation

Just run `yam`

### Usage

Just run `yam tests`. After finding the usage that best describes your usecase, you can inspect `tests/test_exposed.py` and see how the patching was done.
