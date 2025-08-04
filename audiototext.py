from RealtimeSTT import AudioToTextRecorder

def run_recorder(process_text, language='en'):  # for reusability puprpose(importing this in other files)
    # processing
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(language=language)

    while True:
        recorder.text(process_text)

# If run directly
if __name__ == '__main__':
    def default_handler(text):
        print("You said:", text)

    run_recorder(default_handler)
