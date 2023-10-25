def shorten_text():
    text = input()
    return text.replace('-ический', '').replace('-ическая', '')

print(shorten_text())
