#!/usr/bin/env python3


from render_html import *

if __name__ == "__main__":

    output = create_graph("example.txt")
    with open("my_new_file.html", "w") as fh:
        fh.write(output)
