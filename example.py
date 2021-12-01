import curses
import time
import sys
import os

class A():
    def draw(self, stdscr):
        curses.curs_set(0)
        for i in range(10):
            stdscr.addstr(0, 0, f"Hello {i}")
            stdscr.refresh()
            time.sleep(2)

a = A()

print(sys.stdout.isatty())
print(os.environ.get('TERM'))

if sys.stdout.isatty():
    try:
        curses.wrapper(a.draw)
    except curses.error as exc:
        print(exc)
else:
    print("Hello")
