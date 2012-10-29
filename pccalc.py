#!/usr/bin/env python2.7
# encoding: utf-8
'''
pccalc.py

Copyright (c) 2011 Andre Sencioles Vitorio Oliveira <andre@bcp.net.br>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

def parse_args():
    '''Parse the received arguments
    
    Returns a list with the parser object and the arguments dictonary.
    
    '''
    import argparse
    
    parser = argparse.ArgumentParser(description='Converts point code values')
    parser.add_argument('pointcode', metavar='PC', type=int,
                        help='Point code value')
    
    return [parser, vars(parser.parse_args())]

def parse_pc():
  pass
    
def main():
  parser, args = parse_args()
  
  decpc = args.pointcode
  hexpc = hex(args.pointcode)
  binpc = bin(args.pointcode)[2:].zfill(14)
  
  itupc = ['', '', '']
  itupc[0] = str(int('0b'+binpc[0:3],2))
  itupc[1] = str(int('0b'+binpc[3:11],2))
  itupc[2] = str(int('0b'+binpc[11:14],2))
  itupc = '.'.join(itupc)
  
  print 'Dec Point Code       : {0}'.format(decpc)
  print 'Hex Point Code       : {0}'.format(hexpc)
  print 'Bin Point Code       : {0}'.format(binpc)
  print 'ITU 3.8.3 Point Code : {0}'.format(itupc)

if __name__ == '__main__':
    main()
