<p align="center">
  <img src="https://raw.githubusercontent.com/crosstask/CrossTask/main/content/logo_crosstask-removebg.png">
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/crosstask/CrossTask" alt="GitHub code size in bytes" />
  <img src="https://img.shields.io/github/last-commit/crosstask/CrossTask" alt="GitHub last commit" />
  <img src="https://img.shields.io/github/commit-activity/m/crosstask/CrossTask" alt="GitHub commit activity month" />
  <img src="https://img.shields.io/github/license/crosstask/CrossTask" alt="GitHub license" />
</p>



## 📌 Overview

CrossTask is an OpenSource, cross-platform task manager written in Python. It utilizes essential dependencies like customtkinter and psutil.

## 🔍 Table of Contents


- [💻 Stack](#stack)

- [⚙️ Setting Up](#setting-up)

- [🚀 Run Locally](#run-locally)

- [📋 To-Do](#do-do)

- [🙌 Contributors](#contributors)

- [📄 License](#license)


## 📝 Project Summary

- [**config**](config): Configuration files for the project's settings and environment variables.
- [**src**](src): Source code directory containing the main application logic.
- [**src/popups**](src/popups): Contains pop-up related functionality for the application.
- [**src/settings**](src/settings): Module for managing application settings.
- [**cache**](cache): Directory for caching data to improve performance.
- [**content**](content): Stores content files used by the application.
- [**img**](img): Directory for storing image files used in the project.
- [**img/dark**](img/dark): Contains dark-themed image assets.
- [**img/light**](img/light): Contains light-themed image assets.

## 💻 Stack

- [psutil](https://github.com/giampaolo/psutil): Provides an interface for retrieving system information, such as CPU, memory, disk usage, and network statistics.
- [packaging](https://pypi.org/project/packaging/): Provides functionality for working with Python packages, including parsing version numbers, comparing versions, and manipulating package metadata.
- [pillow](https://python-pillow.org/): A fork of the Python Imaging Library (PIL), it provides image processing capabilities, including opening, manipulating, and saving various image file formats.
- [customtkinter](https://github.com/ParthJadhav/customtkinter): A custom version of the tkinter library that adds additional functionalities and styling options to the standard tkinter package.

## 🚀 Run Locally

1.Clone the CrossTask repository:

```sh
git clone https://github.com/crosstask/CrossTask
```

2.Install the dependencies with one of the package managers listed below:

```bash
pip install -r requirements.txt
```

3.Start the development mode:

```bash
python main.py
```

## 📋 To-Do
- [ ] More seperated loading of the tasks
- [ ] Work on settings
- [ ] Auto-reload implementation (integrated via settings)
- [ ] More comments in code
- [ ] GPU integration
- [ ] Show detailed informations for system components
- [ ] Program updater
- [x] Binaries for latest release
- [x] Responsive GUI
- [x] Speed improvements loading tasks into list
- [x] Task informations
- [x] Kill processes
- [x] Popups with developer and version informations

## 🙌 Contributors

<p align="center">
<a href="https://github.com/crosstask/CrossTask/graphs/contributors" target="_blank">
<img src="https://contrib.rocks/image?repo=crosstask/CrossTask" width="15%" alt="" />
</a>
</p>

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [**GNU General Public License v3.0**](https://github.com/crosstask/CrossTask/blob/main/LICENSE) file for details.
