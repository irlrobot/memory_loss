#!/usr/bin/env python
"""
Memory Loss
github.com/irlrobot/memory_loss
"""

QUESTIONS = [
    {
        "question": "Remember these words,  Epic,  Bird,  Taco,  Sphere.  "\
            "Was the second word, bird?",
        "answer": "yes"
    },
#    {
#        "question": "Remember these words,  Map,  Computer,  Fish,  Blimp,  "\
#            "What was the first word?",
#        "answer": "Map",
#        "category": "repeat"
#    },
#    {
#        "id": 87,
#        "question": "Remember these words,  French,  Boat,  Yesterday,  Apple,  "\
#            "What was the second word?",
#        "answer": "Boat",
#        "category": "repeat"
#    },
#    {
#        "id": 88,
#        "question": "Remember these words,  November,  Star,  Dream,  Tuesday,  "\
#            "What was the last word?",
#        "answer": "Tuesday",
#        "category": "repeat"
#    },
#    {
#        "id": 89,
#        "question": "Remember these words,  Drum,  Animal,  Mighty,  Baron,  "\
#            "What was the second word?",
#        "answer": "Animal",
#        "category": "repeat"
#    },
#    {
#        "id": 90,
#        "question": "Remember these words,  Saxophone,  Analysis,  War,  Trumpet,  "\
#            "What was the third word?",
#        "answer": "War",
#        "category": "repeat"
#    },
#    {
#        "id": 91,
#        "question": "Remember these words,  Party,  Fire,  Drink,  Water,  "\
#            "What was the third word?",
#        "answer": "Drink",
#        "category": "repeat"
#    },
#    {
#        "id": 92,
#        "question": "Remember these words,  Answer,  Phone,  Cancel,  Shower,  "\
#            "What was the first word?",
#        "answer": "Answer",
#        "category": "repeat"
#    },
#    {
#        "id": 93,
#        "question": "Remember these words,  Think,  Observe,  Sleep,  Pizza,  "\
#            "What was the last word?",
#        "answer": "Pizza",
#        "category": "repeat"
#    },
#    {
#        "id": 94,
#        "question": "Remember these words,  Pressure,  Pants,  Advance,  Game,  "\
#            "What was the second word?",
#        "answer": "Pants",
#        "category": "repeat"
#    },
#    {
#        "id": 95,
#        "question": "Remember these words,  Moment,  Win,  Heat,  Growth,  "\
#            "What was the third word?",
#        "answer": "Heat",
#        "category": "repeat"
#    },
#    {
#        "id": 96,
#        "question": "Remember these numbers,  7,  2,  11,  4,  "\
#            "What was the lowest number?",
#        "answer": "2",
#        "category": "low_high_number"
#    },
#    {
#        "id": 97,
#        "question": "Remember these numbers,  3,  1,  9,  8,  "\
#            "What was the highest number?",
#        "answer": "9",
#        "category": "low_high_number"
#    },
#    {
#        "id": 98,
#        "question": "Remember these numbers,  12,  15,  18,  6,  "\
#            "What was the highest number?",
#        "answer": "18",
#        "category": "low_high_number"
#    },
#    {
#        "id": 99,
#        "question": "Remember these numbers,  17,  14,  15,  13,  "\
#            "What was the lowest number?",
#        "answer": "13",
#        "category": "low_high_number"
#    },
#    {
#        "id": 100,
#        "question": "Remember these numbers,  3,  8,  5,  4,  "\
#            "What was the lowest number?",
#        "answer": "3",
#        "category": "low_high_number"
#    },
#    {
#        "id": 101,
#        "question": "Remember these numbers,  13,  28,  18,  23,  "\
#            "What was the highest number?",
#        "answer": "28",
#        "category": "low_high_number"
#    },
#    {
#        "id": 102,
#        "question": "Remember these numbers,  6,  9,  5,  2,  "\
#            "What was the highest number?",
#        "answer": "9",
#        "category": "low_high_number"
#    },
#    {
#        "id": 103,
#        "question": "Remember these numbers,  37,  32,  38,  34,  "\
#            "What was the lowest number?",
#        "answer": "32",
#        "category": "low_high_number"
#    },
#    {
#        "id": 104,
#        "question": "Remember these numbers,  5,  7,  1,  3,  "\
#            "What was the highest number?",
#        "answer": "7",
#        "category": "low_high_number"
#    },
#    {
#        "id": 105,
#        "question": "Remember these numbers,  27,  22,  28,  25,  "\
#            "What was the lowest number?",
#        "answer": "22",
#        "category": "low_high_number"
#    },
#    {
#        "id": 106,
#        "question": "Remember these numbers,  13,  28,  18,  23. "\
#            "Was the third number 38?",
#        "answer": "no",
#        "category": "repeat"
#    },
#    {
#        "id": 107,
#        "question": "Remember these numbers,  6,  9,  5,  2. "\
#            "Was the second number 9?",
#        "answer": "yes",
#        "category": "repeat"
#    },
#    {
#        "id": 108,
#        "question": "Remember these numbers,  37,  32,  38,  34. "\
#            "Was the second number 38?",
#        "answer": "no",
#        "category": "repeat"
#    },
#    {
#        "id": 109,
#        "question": "Remember these numbers,  5,  7,  1,  3. "\
#            "Was the third number 1?",
#        "answer": "yes",
#        "category": "repeat"
#    },
    {
        "question": "Remember these numbers,  27,  22,  28,  25. "\
            "Was the first number 26?",
        "answer": "no"
    }
]
