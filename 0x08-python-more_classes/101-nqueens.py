#!/usr/bin/python3
import sys
"""This module attempts to solve the famous N queens puzzle
The N queens puzzle is the challenge of placing N non-attacking queens on
an N x N chessboard
"""
if len(sys.argv) != 2:
    print("Usage: nqueens N\n")
    sys.exit(1)
try:
    c = int(sys.argv[1])
except ValueError:
    print("N must be a number\n")
    sys.exit(1)
if c < 4:
    print("N must be at least 4\n")
    sys.exit(1)
