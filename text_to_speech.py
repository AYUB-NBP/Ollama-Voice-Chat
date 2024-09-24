import asyncio
import edge_tts
import sys
from langdetect import detect
import random

TEXT = ' '.join(sys.argv[1:])

#Depending on detected language, choose voice accordingly
lang = detect(TEXT)

match lang:
    case 'en':
        en_voices=['en-AU-NatashaNeural', 'en-AU-WilliamNeural', 'en-CA-ClaraNeural', 'en-CA-LiamNeural', 'en-GB-LibbyNeural', 'en-GB-MaisieNeural', 'en-GB-RyanNeural', 'en-GB-SoniaNeural', 'en-GB-ThomasNeural', 'en-HK-SamNeural', 'en-HK-YanNeural', 'en-IE-ConnorNeural', 'en-IE-EmilyNeural', 'en-IN-NeerjaExpressiveNeural', 'en-IN-NeerjaNeural', 'en-IN-PrabhatNeural', 'en-KE-AsiliaNeural', 'en-KE-ChilembaNeural', 'en-NG-AbeoNeural', 'en-NG-EzinneNeural', 'en-NZ-MitchellNeural', 'en-NZ-MollyNeural', 'en-PH-JamesNeural', 'en-PH-RosaNeural', 'en-SG-LunaNeural', 'en-SG-WayneNeural', 'en-TZ-ElimuNeural', 'en-TZ-ImaniNeural', 'en-US-AnaNeural', 'en-US-AndrewMultilingualNeural', 'en-US-AndrewNeural', 'en-US-AriaNeural', 'en-US-AvaMultilingualNeural', 'en-US-AvaNeural', 'en-US-BrianMultilingualNeural', 'en-US-BrianNeural', 'en-US-ChristopherNeural', 'en-US-EmmaMultilingualNeural', 'en-US-EmmaNeural', 'en-US-EricNeural', 'en-US-GuyNeural', 'en-US-JennyNeural', 'en-US-MichelleNeural', 'en-US-RogerNeural', 'en-US-SteffanNeural', 'en-ZA-LeahNeural', 'en-ZA-LukeNeural']
        voice_index = random.randint(0,len(en_voices)-1)
        VOICE =en_voices[voice_index] #Generate a random Voice for variety
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