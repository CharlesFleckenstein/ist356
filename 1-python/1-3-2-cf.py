def cleanup(text : str) -> str:
    for ch in "!,?":
        text = text.replace(ch, '')
    lower_text = text.lower()
    short_text = lower_text.lstrip(' ').rstrip(' ')
    return lower_text
                              
words = ' hello! ?world   ! '
c = cleanup(words)
print(c)