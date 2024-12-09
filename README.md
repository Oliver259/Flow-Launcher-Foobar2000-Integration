# Foobar2000 Integration Plugin

This plugin allows you to control foobar2000 from Flow Launcher using the Beefweb plugin.

## Installation

### Prerequisites

1. **Flow Launcher**: You can find it [here](https://github.com/Flow-Launcher/Flow.Launcher)
2. **Foobar2000**: Ensure you have foobar2000 installed on your system.
3. **Beefweb Plugin**: Install the Beefweb plugin for foobar2000. You can find it [here](https://github.com/hyperblast/beefweb).

### Manual Installation

1. **Download the Plugin**:
   - Download the plugin files from the repository.

2. **Create a `lib` Directory**:
   - Navigate to the plugin directory and create a `lib` folder.

3. **Install Dependencies**:
   - Use `pip` to install the required dependencies into the `lib` folder:
     ```sh
     pip install -r requirements.txt -t ./lib
     ```

4. **Move the Plugin to Flow Launcher Plugins Directory**:
   - Move the entire plugin folder to the Flow Launcher plugins directory:
     - On Windows: `%APPDATA%\FlowLauncher\Plugins`
     - On Linux: `~/.config/FlowLauncher/Plugins`

5. **Restart Flow Launcher**:
   - Restart Flow Launcher to load the new plugin.

## Usage

- `fb play`: Play music in foobar2000.
- `fb pause`: Pause music in foobar2000.
- `fb stop`: Stop music in foobar2000.
- `fb next`: Play the next track in foobar2000.
- `fb previous`: Play the previous track in foobar2000.
- `fb random`: Play a random track in foobar2000.
- `fb current`: Show the currently playing track in foobar2000.

## Development

### Project Structure
```bash
├── Images
│   ├── app.png
│   └── foobar2000.png
├── README.md
├── lib
│   ├── flowlauncher
│   │   ├── FlowLauncher.py
│   │   ├── FlowLauncherAPI.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── FlowLauncher.cpython-310.pyc
│   │   │   ├── FlowLauncherAPI.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── _version.cpython-310.pyc
│   │   └── _version.py
│   └── flowlauncher-0.2.0.dist-info
│       ├── INSTALLER
│       ├── LICENSE
│       ├── METADATA
│       ├── RECORD
│       ├── REQUESTED
│       ├── WHEEL
│       └── top_level.txt
├── plugin.json
├── requirements.txt
├── run.py
└── tree.txt
```


### `plugin.json`

Ensure your `plugin.json` includes the necessary metadata:

```json
{
    "ID": "unique-id",
    "ActionKeyword": "fb",
    "Name": "Foobar2000 Integration",
    "Description": "Control foobar2000 from Flow Launcher using Beefweb",
    "Author": "Your Name",
    "Version": "1.0.0",
    "Language": "python",
    "Website": "https://github.com/your-repo/foobar2000-plugin",
    "IcoPath": "Images/app.png",
    "ExecuteFileName": "run.py"
}
```

### `requirements.txt`
Ensure your `requirements.txt` includes all necessary dependencies: ```flowlauncher```