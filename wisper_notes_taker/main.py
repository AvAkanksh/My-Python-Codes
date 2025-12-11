import whisper
import pyaudio
import numpy as np

# Load Whisper model
model = whisper.load_model("base")  # Use 'small', 'medium', or 'large' for better accuracy

# Audio settings
CHUNK = 1024  # Buffer size
FORMAT = pyaudio.paInt16  # 16-bit audio format
CHANNELS = 1  # Mono audio
RATE = 16000  # Sampling rate (16 kHz)

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Listening...")

# Function to transcribe audio
def transcribe_audio(audio_data):
    # Convert to numpy array
    audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
    # Transcribe using Whisper
    result = model.transcribe(audio_np, fp16=False, language=None)  # or set language explicitly
    return result["text"]

try:
    audio_buffer = b""
    while True:
        # Read audio stream
        data = stream.read(CHUNK)
        audio_buffer += data

        # Process in chunks of ~5 seconds
        if len(audio_buffer) >= RATE * 5:  # 5 seconds of audio
            text = transcribe_audio(audio_buffer)
            print(f"Transcript: {text}")
            audio_buffer = b""  # Clear the buffer
except KeyboardInterrupt:
    print("\nStopping transcription...")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
