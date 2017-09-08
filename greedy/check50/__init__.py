from check50 import *

class Greedy(Checks):

    @check()
    def exists(self):
        """greedy.c exists"""
        self.require("greedy.c")

    @check("exists")
    def compiles(self):
        """greedy.c compiles"""
        self.spawn("clang -o greedy greedy.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_41_cents(self):
        """input of 0.41 yields output of 4"""
        self.spawn("./greedy").stdin("0.41").stdout("4\n", "4\n").exit(0)