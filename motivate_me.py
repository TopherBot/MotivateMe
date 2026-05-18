#!/usr/bin/env python3
"""MotivateMe – print a random motivational quote.

Usage:
    python3 motivate_me.py
"""
import random

QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Hard work beats talent when talent doesn't work hard. – Tim Notke",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The future depends on what you do today. – Mahatma Gandhi",
]

def main():
    print(random.choice(QUOTES))

if __name__ == "__main__":
    main()
