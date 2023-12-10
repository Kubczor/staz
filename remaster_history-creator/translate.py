import os
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"history-creator_key.json"

translate_client = translate_v2.Client()

text = "Kocham Cie"

target = "pl"

translation = translate_client.translate(text, target_language=target)

translated_text = translation['translatedText']
print(f"Tłumaczenie: {translated_text}")
