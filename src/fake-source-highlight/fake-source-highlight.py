#!/usr/bin/env python

# Fake for source-highlight that wraps stdin in <pre></pre> block only. To use, uninstall gnu source-highlighter and copy this to path.

import sys

write = sys.stdout.write
write('<pre>')
content = sys.stdin.read()
content = content.rstrip('\n')
write(content)
write('</pre>')
sys.exit(0)
