import curses
import time

class A():
    def draw(self, stdscr):
        curses.curs_set(0)
        for i in range(10):
            stdscr.addstr(0, 0, f"Hello {i}")
            stdscr.refresh()
            time.sleep(2)

a = A()
curses.wrapper(a.draw)
