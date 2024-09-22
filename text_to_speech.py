import asyncio
import edge_tts
import sys
from langdetect import detect

TEXT = ' '.join(sys.argv[1:])

#Depending on detected language, choose voice accordingly
lang = detect(TEXT)

match lang:
    case 'en':
        VOICE ='en-GB-SoniaNeural'
    case 'de':
        VOICE ='de-DE-ConradNeural'
    case 'fr':
        VOICE = 'fr-FR-HenriNeural'
    case 'es':
        VOICE = 'es-MX-DaliaNeural'
    case 'ar':
        VOICE = 'ar-AE-FatimaNeural'
    case _:
        VOICE ='en-GB-SoniaNeural'
    
OUTPUT_FILE = "tts.mp3"

############################################ 

characters_to_ignore = ['*']
for c in characters_to_ignore:
    TEXT = TEXT.replace(c,'')

############################################

async def amain() -> None:
    #Main function
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    asyncio.run(amain())