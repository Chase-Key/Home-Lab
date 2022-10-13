import cowsay
import sys
"""
Cowsay Characters:
- cow, trex, beavis, cheese, daemon, dragon, fox, ghostbusters,
kitty, meow, miki, pig, stegosaurus, stimpy, turkey, turtle, tux
"""

if len(sys.argv) == 2:
    cowsay.tux("hello, " + sys.argv[1])
