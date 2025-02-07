import tty
import sys
import termios

tty_attrs = termios.tcgetattr(0)
tty.setcbreak(0)


def run():
    while True:
        ch = sys.stdin.read(1)
        if "1" <= ch <= "9":
            for _ in range(int(ch)):
                sys.stdout.buffer.write(b"\x07")
        sys.stdout.buffer.flush()


try:
    run()
finally:
    termios.tcsetattr(0, termios.TCSADRAIN, tty_attrs)
