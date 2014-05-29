#!/usr/bin/env python

# Fake for source-highlight that wraps stdin in <pre></pre> block only. To use, uninstall gnu source-highlighter and copy this to path.

import sys, getopt, cgi

def main(argv):
  lang=''

  try:
    opts, args = getopt.getopt(argv,"f:s:",["line-number="])
  except getopt.GetoptError:
    print 'source-highlight -f <ignored> -s <source language> --line-number <ignored>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-s':
      lang = arg

  if lang == '':
    print 'lang not set!'
    sys.exit(2)

  write = sys.stdout.write
  write('<pre class="lang:{lang}">'.format(lang=lang))
  content = sys.stdin.read()
  content = content.rstrip('\n')
  content = cgi.escape(content).encode('ascii','xmlcharrefreplace')
  write(content)
  write('</pre>')

if __name__ == "__main__":
   main(sys.argv[1:])
