# 📘 Day 13

## Pyttsx3 Module

## Table of Contents
1. [What is pyttsx3](#what-is-pyttsx3)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Platform-Specific Notes](#platform-specific-notes)
5. [Additional Resources](#additional-resources)

---

# What is pyttsx3?

pyttsx3 is a text-to-speech (TTS) library for Python that works offline. It converts text into spoken words using your computer's built-in speech engines without requiring an internet connection.

**Use cases:**
- Virtual assistants
- Accessibility tools
- Audio book readers
- Educational applications
- Voice notifications
- Interactive games

## Installation

### With UV (recommended)

```bash
# Create project
uv init voice-app
cd voice-app

# Add pyttsx3
uv add pyttsx3

# For Mac users (may need additional dependencies)
# pyttsx3 uses the system's built-in TTS, so usually no extra deps needed
```

### Mac-Specific Notes

On Mac Apple Silicon, pyttsx3 uses the native `nsss` engine which is already installed with macOS.

### Project Structure

```
voice-app/
├── .venv/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── speaker.py
│   └── assistant.py
└── README.md
```

## Basic Concepts

### 1. Simple Text-to-Speech

```python
import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Speak text
engine.say("Hello, World!")
engine.runAndWait()
```

### 2. Speak Multiple Lines

```python
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello, my name is Assistant.")
engine.say("How can I help you today?")
engine.runAndWait()
```

### 3. Get Available Voices

```python
import pyttsx3

engine = pyttsx3.init()

# Get all available voices
voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")
    print(f"   ID: {voice.id}")
    print(f"   Languages: {voice.languages}")
    print()
```

### 4. Change Voice

```python
import pyttsx3

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Set voice (0 is usually male, 1 is usually female)
engine.setProperty('voice', voices[1].id)

engine.say("I am using a different voice now")
engine.runAndWait()
```

### 5. Adjust Speech Rate

```python
import pyttsx3

engine = pyttsx3.init()

# Get current rate
rate = engine.getProperty('rate')
print(f"Current rate: {rate}")

# Set slower rate
engine.setProperty('rate', 150)  # Default is usually 200
engine.say("I am speaking slowly")
engine.runAndWait()

# Set faster rate
engine.setProperty('rate', 250)
engine.say("I am speaking quickly")
engine.runAndWait()
```

### 6. Adjust Volume

```python
import pyttsx3

engine = pyttsx3.init()

# Get current volume (0.0 to 1.0)
volume = engine.getProperty('volume')
print(f"Current volume: {volume}")

# Set volume to 50%
engine.setProperty('volume', 0.5)
engine.say("I am speaking at half volume")
engine.runAndWait()

# Set volume to 100%
engine.setProperty('volume', 1.0)
engine.say("I am speaking at full volume")
engine.runAndWait()
```

## Platform-Specific Notes

### macOS
- Uses `nsss` engine (native)
- Voices located in System Preferences → Accessibility → Speech
- Usually works out of the box

## Additional Resources

### Official Documentation
- [pyttsx3 PyPI](https://pypi.org/project/pyttsx3/)
- [pyttsx3 GitHub](https://github.com/nateshmbhat/pyttsx3)

### Related Libraries
- `speech_recognition` - Speech to text (complement to pyttsx3)
- `gTTS` - Google Text-to-Speech (requires internet)
- `playsound` - Play audio files

### Useful Combinations
- pyttsx3 + speech_recognition = Voice assistant
- pyttsx3 + tkinter = GUI applications
- pyttsx3 + pygame = Games with voice


[<< Day 12](../day_12/day_12.md) | [Day 14 >>](../day_14/day_14.md)