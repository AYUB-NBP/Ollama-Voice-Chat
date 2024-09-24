from project import *
import time



def test_is_process_running():
    assert is_process_running('qsldjksqq.exe') == False
    assert is_process_running('explorer.exe') == True

def test_kill_process_by_name():
    subprocess.run('notepad.exe')
    time.sleep(1)
    assert is_process_running('notepad.exe') == True
    kill_process_by_name('notepad.exe')
    time.sleep(1)
    assert is_process_running('notepad.exe') == False

def test_ollama_server():
    assert ollama_server('Hi there') #Server responds

    
    


