import sounddevice as sd # for recording user's voice
import numpy as np #Necessary for Wavio
import whisper   # for voice transcribing/recognition
import keyboard  # for detecting keyboard input
import wavio     # to save audio as a .wav file


def main():

    filename = "recorded_audio.wav"

    # Record audio with push-to-talk
    bool = record_audio(filename)

    # Transcribe the recorded audio

    if bool:
        transcript = transcribe_audio(filename)
        return transcript
    
# Set parameters for audio recording
sample_rate = 16000  # Sample rate for Whisper (16kHz)

def record_audio(filename):
    # Records audio and saves it to a .wav file
    print("Press and hold left shift to start recording... or press Esc (Escape) to type a prompt")
    frames = []

    # Start recording when left shift is pressed
    while True:
        if keyboard.is_pressed('left shift'):
            print("Recording (Release left shift to stop)\n")
            with sd.InputStream(samplerate=sample_rate, channels=1, dtype=np.int16) as stream:
                while keyboard.is_pressed('left shift'):
                    data, _ = stream.read(1024)  # Read chunks of data
                    frames.append(data)
            break
        elif keyboard.is_pressed('escape'):
            break

    if frames:
        # Convert the list of frames to a numpy array
        try:
            frames = np.concatenate(frames)
        except ValueError:
            pass

        # Saving the recorded audio
        wavio.write(filename, frames, sample_rate, sampwidth=2)
        # print(f"Recording saved to {filename}")
        return True
    else:
        return False

def transcribe_audio(filename):
    """Transcribes audio using Whisper"""
    # Whisper model initialization
    model = whisper.load_model("small")  # You can choose 'small', 'medium', 'large', etc.
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(filename)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language=max(probs, key=probs.get)
    # print(f"Detected language: {detected_language}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    if result.text == 'you':
        return ''
    else:
        print(result.text)
        return result.text

if __name__ == "__main__":
    main()