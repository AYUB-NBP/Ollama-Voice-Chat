import ollama
import sys
import psutil
import subprocess
import voice_recognition
import os

    #MAIN GOAL

# I wanna be able to speak to a chatbot using my voice and replicate the feature of chatGPT on PC.

    #Milestones:

# - Be able to intereact with the LLM using python and text
# - Find a way to substitute typed text with spoken words.(Speech to text)
# - inject Speech in bot
# - Get Answer
# - Get spoken answer.
# - Add Tests
# - Debug
# - Simplify code and comments modifications
# - GUI?!, maybe... flask web app
# - History
# - Context memory
# - Change Voice depending on sentence language ( adaptive TTS, useful for language learning)

##########################################################################################

#The value of 'venv' must match the name of you virtual environement directory.
venv = 'venv'

def main():
        state = is_process_running('ollama.exe')
        if state:    
            print("Welcome to Ollama live chat. Type 'exit()' to stop chatting or use CTRL+C \n -----------------------------------------------")
            run_Ollama()
        else :
            subprocess.Popen('server.bat')
            
            run_Ollama()
            
def ollama_server(_prompt):
        stream = ollama.generate(model='llama3.1:8b' ,prompt=_prompt,stream=True,context=[1, 2, 3])
        full_response=[] #Initialising word list
        for chunk in stream:
            word = chunk['response']
            print(word, end='', flush=True)
            full_response.append(word)
        print('\n')
        response_string = ''.join(str(x) for x in full_response).replace('*','')
        return response_string

def is_process_running(process_name):
    # Iterate over all running processes
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

def kill_process_by_name(process_name):
    subprocess.run(['taskkill', '/F', '/IM', process_name])

def run_Ollama():
    try: #Preventing an ugly exception from appearing after CTRL+C
        prompt = voice_recognition.main()

        if not prompt:
            prompt = input('User: ').strip()

        if prompt.lower() == 'exit()':
            processes = ['ollama.exe','ollama_llama_server.exe','ollama app.exe','WindowsTerminal.exe','python.exe']
            clean_up()
            for process in processes:
                kill_process_by_name(process)
            #Delete Audio files used for Voice recognition and TTS
            
            sys.exit(0)
        elif prompt == None or prompt == '' or prompt == 'you':
            run_Ollama()
        #MAIN BIT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        response_string = ollama_server(prompt)
        #TTS part
        subprocess.run(f"""{venv}\\Scripts\\python.exe text_to_speech.py {response_string}""")

        #play the TTS
        try:
            play_audio()
        except KeyboardInterrupt:
            run_Ollama()

        #Delete Audio files used for Voice recognition and TTS
        clean_up()
        
        run_Ollama() #loop all the way back to the beginning
    except KeyboardInterrupt:
        print('Goodbye!')
        clean_up()
        sys.exit(0)
    
    if response_string:
        return True #Response 
    else:
        return False

def play_audio():
    # Run ffplay in a subprocess
    subprocess.call(r'ffplay -nodisp -autoexit -loglevel quiet "tts.mp3"')
def clean_up():
    audio_files = ['recorded_audio.wav','tts.mp3']
    for file in audio_files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    main()
    