import os
import json
from deep_translator import GoogleTranslator

def translate_json(input_file, output_directory, target_languages):
    # Load the input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Translate each string in the JSON for each target language
    for language in target_languages:
        translated_data = {}
        translator = GoogleTranslator(source='auto', target=language)
        chunk_size = 10
 
        chunks = []
        for key, value in data.items():
            chunks.append((key, value))
            if len(chunks) == chunk_size or len(data) == len(chunks):
                translated = translator.translate_batch(list(zip(*chunks))[1])
                keys = list(zip(*chunks))[0]
                for i in range(len(keys)):
                    translated_data[keys[i]] = translated[i]
                print("total translated", len(translated_data))
                # translated_data.update()
                chunks = []
        # return

        # create output directory if it doesn't exist with language name
        if not os.path.exists(os.path.join(output_directory, language)):
            os.makedirs(os.path.join(output_directory, language))
        # Save the translated JSON
        output_file = os.path.join(output_directory, language, filename)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=4)

        print(f'Translated JSON saved to {output_file}')

if __name__ == '__main__':
    input_directory = input("Enter the directory containing input JSON files: ")
    output_directory = input("Enter the directory to save the translated JSON files: ")
    target_languages = input("Enter the target languages separated by commas (e.g., 'fr,es,de'): ").split(',')

    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            input_file = os.path.join(input_directory, filename)
            translate_json(input_file, output_directory, target_languages)
