import pyaudio
import wave
import threading

class AudioHandler:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.pyaudio_instance = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False

    def start_recording(self, filename):
        """Starts recording audio to a file."""
        self.is_recording = True
        self.stream = self.pyaudio_instance.open(format=self.format, channels=self.channels,
                                                 rate=self.rate, input=True,
                                                 frames_per_buffer=self.chunk)

        def record():
            wf = wave.open(filename, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(self.format))
            wf.setframerate(self.rate)

            while self.is_recording:
                wf.writeframes(self.stream.read(self.chunk))

            wf.close()
            self.stream.stop_stream()
            self.stream.close()

        threading.Thread(target=record).start()

    def stop_recording(self):
        """Stops the recording."""
        self.is_recording = False

    def play_audio(self, filename):
        """Plays an audio file."""
        wf = wave.open(filename, 'rb')
        stream = self.pyaudio_instance.open(format=self.pyaudio_instance.get_format_from_width(wf.getsampwidth()),
                                            channels=wf.getnchannels(),
                                            rate=wf.getframerate(),
                                            output=True)

        data = wf.readframes(self.chunk)
        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)

        stream.stop_stream()
        stream.close()
        wf.close()

    def close(self):
        """Closes PyAudio instance."""
        self.pyaudio_instance.terminate()

# Example usage
if __name__ == "__main__":
    audio_handler = AudioHandler()
    try:
        audio_handler.start_recording("test.wav")
        input("Recording... press Enter to stop.\n")
        audio_handler.stop_recording()
        audio_handler.play_audio("test.wav")
    finally:
        audio_handler.close()
