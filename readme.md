

# Localization Translator

This Python script translates JSON files into multiple languages using the Google Translator API provided by the `deep_translator` library.

## Features

- Translates JSON files into multiple languages.
- Supports batch translation for improved performance.
- Saves translated JSON files in the specified output directory.

## Installation

1. Install Python (if not already installed). You can download it from [python.org](https://www.python.org/).
2. Install the required dependencies using pip:
    ```bash
    pip install deep_translator
    ```

## Usage

1. Clone this repository or download the `translator.py` file.
2. Navigate to the directory containing the `translator.py` file in your terminal.
3. Run the script using Python:
    ```bash
    python translator.py
    ```
4. Follow the prompts to provide the input directory containing JSON files, the output directory to save translated JSON files, and the target languages separated by commas.

## Example

```bash
python translator.py
```

```
Enter the directory containing input JSON files: input_data
Enter the directory to save the translated JSON files: output_data
Enter the target languages separated by commas (e.g., 'fr,es,de'): fr,es,de
```

## Requirements

- Python 3.x
- `deep_translator` library

## Credits

This script was developed by [MD Shadhin Mia](https://github.com/md-shadhin-mia).
