from speech_engine.recognizer import listen
from speech_engine.speaker import speak
from command_engine.command_handler import handle_command
from config import WAKE_WORD, ASSISTANT_NAME, EXIT_COMMANDS


def run_assistant():

    speak(f"Hello Hariram, I am {ASSISTANT_NAME}. How can I help you?")

    while True:
        command = listen()

        if command == "":
            continue

        if any(exit_word in command for exit_word in EXIT_COMMANDS):
            speak("Goodbye Hariram!")
            break

        if WAKE_WORD in command:
            command = command.replace(WAKE_WORD, "").strip()
            handle_command(command)


if __name__ == "__main__":
    run_assistant()