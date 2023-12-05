import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    print("Enter the word you want to speak it out by computer (type 'exit' to end):")
    s = input()

    if s.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    speaker.Speak(s)
