import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keys = {
    "A": Keycode.A, "B": Keycode.B, "C": Keycode.C, "D": Keycode.D, "E": Keycode.E,
    "F": Keycode.F, "G": Keycode.G, "H": Keycode.H, "I": Keycode.I, "J": Keycode.J,
    "K": Keycode.K, "L": Keycode.L, "M": Keycode.M, "N": Keycode.N, "O": Keycode.O,
    "P": Keycode.P, "Q": Keycode.Q, "R": Keycode.R, "S": Keycode.S, "T": Keycode.T,
    "U": Keycode.U, "V": Keycode.V, "W": Keycode.W, "X": Keycode.X, "Y": Keycode.Y,
    "Z": Keycode.Z,

    "1": Keycode.ONE, "2": Keycode.TWO, "3": Keycode.THREE, "4": Keycode.FOUR,
    "5": Keycode.FIVE, "6": Keycode.SIX, "7": Keycode.SEVEN, "8": Keycode.EIGHT,
    "9": Keycode.NINE, "0": Keycode.ZERO,

    "ENTER": Keycode.ENTER,
    " ": Keycode.SPACE,
    "BORRAR": Keycode.BACKSPACE,
    "TAB": Keycode.TAB,
    "ESC": Keycode.ESCAPE,
    "SHIFT": Keycode.SHIFT,
    "CTRL": Keycode.CONTROL,
    "ALT": Keycode.ALT,
    "WINDOWS": Keycode.GUI,
    "MAYUS": Keycode.CAPS_LOCK,

    "ARRIBA": Keycode.UP_ARROW,
    "ABAJO": Keycode.DOWN_ARROW,
    "IZQUIERDA": Keycode.LEFT_ARROW,
    "DERECHA": Keycode.RIGHT_ARROW,
}

def separar_instrucciones(filename):
    try:
        lines = [line.strip() for line in open(filename, "r").readlines()]
    except FileNotFoundError:
        return []
    return lines

kbd = Keyboard(usb_hid.devices)
archivo = separar_instrucciones("juas.txt")

for line in archivo:
    if line.startswith("STRING "):
        texto = line[len("STRING "):]
        for char in texto:
            kbd.press(Keycode.SHIFT) if char.isupper() else None
            kbd.send(keys.get(char.upper(), None)) if char.upper() in keys else None
            kbd.release_all()
            time.sleep(0.02)

    else:
        partes = line.split()
        teclas = []
        for p in partes:
            tecla = keys.get(p.upper())
            if tecla:
                teclas.append(tecla)

        if teclas:
            kbd.send(*teclas)
        time.sleep(0.5)