# Icon Changer

A Python application that automatically downloads and sets icons for folders based on their names using Google Custom Search.

## Features

- User-friendly graphical interface
- Automatically searches for images based on folder name
- Downloads and converts images to icon format
- Sets folder icons (Windows only)

## Requirements

- Python 3.x
- Tkinter (for GUI)
- Google API Key and Custom Search Engine ID
- Required Python packages: requests, google-api-python-client, pillow

## Installation

1. Clone this repository:
```
git clone https://github.com/Mohsin241002/icon-changer.git
cd icon-changer
```

2. Create and activate a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install requests google-api-python-client pillow
```

4. Make sure you have Tkinter installed:
   - On macOS: `brew install python-tk`
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On Windows: Tkinter comes pre-installed with Python

## Usage

1. Run the application:
```
python check3.py
```

2. Use the interface to:
   - Select a folder
   - The application will download an image based on the folder name
   - The image will be converted to an icon format (.ico)

3. Note: The folder icon changing functionality works only on Windows. On macOS and Linux, the icons will be downloaded but not automatically applied to folders.

## Platform Compatibility

- **Windows**: Full functionality - downloads icons and changes folder icons
- **macOS/Linux**: Partial functionality - downloads and converts icons but doesn't change folder icons (the `attrib` command is Windows-specific)

## Customization

The Google Custom Search settings can be modified in the script:

```python
# Set your API key and search engine ID
api_key = "YOUR_API_KEY"
search_engine_id = "YOUR_SEARCH_ENGINE_ID"
```

Replace with your own Google API key and Custom Search Engine ID for continued usage. 