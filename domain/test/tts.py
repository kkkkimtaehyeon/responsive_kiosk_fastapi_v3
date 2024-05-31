import pyaudio
import queue
import threading
from openai import OpenAI

def play_audio_data(pya, audio_queue):
    """ Plays audio chunks from the queue. """
    stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=24000, output=True)
    while True:
        chunk = audio_queue.get()
        if chunk is None:  # Sentinel value to stop the playback
            break
        stream.write(chunk)
    stream.stop_stream()
    stream.close()

def stream_audio(model: str, voice: str, input_text: str, initial_buffer_size: int = 150000):
    pya = pyaudio.PyAudio()
    audio_queue = queue.Queue()

    client = OpenAI(api_key="")

    with client.audio.speech.with_streaming_response.create(
        model=model,
        voice=voice,
        input=input_text,
        response_format='wav'
    ) as response:
        buffer = b''  # Temporary buffer to accumulate initial chunks
        playback_started = False
        play_thread = None

        # Process each chunk only once
        for chunk in response.iter_bytes():
            if not playback_started:
                buffer += chunk
                # Check if initial buffer is sufficiently filled
                if len(buffer) >= initial_buffer_size:
                    # Start the playback thread once the buffer size is reached
                    audio_queue.put(buffer)  # Send the initial buffer to the queue
                    play_thread = threading.Thread(target=play_audio_data, args=(pya, audio_queue))
                    play_thread.start()
                    playback_started = True
                    buffer = b''  # Clear the initial buffer since it's now in the queue
            else:
                audio_queue.put(chunk)

        if not playback_started:
            # If the stream ends before filling the initial buffer, start playback with whatever we have
            audio_queue.put(buffer)
            play_thread = threading.Thread(target=play_audio_data, args=(pya, audio_queue))
            play_thread.start()

        # End signal for the playback thread
        audio_queue.put(None)
        if play_thread:
            play_thread.join()

        # Cleanup
        pya.terminate()

# Usage
stream_audio(model="tts-1", voice="alloy", input_text="안녕하세요 저는 open ai 사의 음성 합성 시스템입니다.")