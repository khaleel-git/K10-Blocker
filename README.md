# K10-Blocker

## Project Description

K10-Blocker is a utility designed to block or restrict certain processes or applications on a system. It's built to provide users with fine-grained control over their environment, ensuring that specified software or services do not run. This tool is particularly useful for managing resources, enhancing security, or maintaining system stability by preventing unwanted executables from launching.

## Features

* **Process Blocking:** Dynamically block specific `.exe` or other executable files from running.

* **System-level Integration:** Operates at a low level to effectively prevent applications from launching.

* **Easy Configuration:** Simple configuration file to add or remove applications from the block list.

* **Cross-platform (if applicable):** Designed with cross-platform compatibility in mind.

## Installation

This project is likely a Python application, so these instructions assume you have Python and `pip` installed.

1. **Clone the Repository**
   Start by cloning the repository to your local machine:

```

git clone https://github.com/khaleel-git/K10-Blocker.git
cd K10-Blocker

```

2. **Create a Virtual Environment (Recommended)**
It's best practice to work within a virtual environment to manage dependencies:

```

# On Windows

python -m venv venv
venv\\Scripts\\activate

# On macOS/Linux

python3 -m venv venv
source venv/bin/activate

```

3. **Install Dependencies**
Install all required packages using `pip`. You will need a `requirements.txt` file in your repository for this to work.

```

pip install -r requirements.txt

```

## Usage

Once installed, you can run the application from the command line.

### Basic Execution

To start the blocker, simply run the main script.

```

python main.py

```

### Configuration

The list of applications to block is controlled by a configuration file (e.g., `config.json` or `blocked_apps.txt`). Open this file and add the filenames of the executables you want to block, one per line.

```

# Example content of a configuration file

K10\_Blocker.exe
another\_app.exe
unwanted\_service.exe

```

The application will read this file on startup and block any processes that match the names listed.

## Contributing

We welcome contributions! If you have a suggestion for an improvement, a bug report, or want to add a new feature, please feel free to:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/your-feature-name`).

3. Make your changes and commit them (`git commit -m 'Add new feature'`).

4. Push to the branch (`git push origin feature/your-feature-name`).

5. Open a Pull Request.

## Contact

For questions or issues, please open an issue on the GitHub repository.
```
