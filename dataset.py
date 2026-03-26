"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",

    #*Add 5-10 new posts to SAMPLE_POSTS that reflect realistic language: slang, emojis, mixed emotions, or subtle tone.
    "Lowkey stressed but kind of proud of myself",
    "Just had the best coffee ever! :)",
    "This movie is so bad it's good",
    "Feeling like a million bucks today! 💰",
    "Why does everything have to be so hard?",

    #* experimental: add more posts here ambiguous that depend on feeling and tone of voice to interpret, and hard to label even for a human. 
    "I'm not sure how I feel about this...",
    "Well, that was unexpected.",
    "I guess it could be worse.",
    "I can't believe this happened! 😂",
    "This is the best day ever... or is it? 🤔",
    "I'm really not sure about this.",
    "This is kind of a mess, but also kind of fun.",
    "I absolutely love getting stuck in traffic"  ,
    "This is so bad, it's actually kind of amazing",
    "I don't know whether to laugh or cry about this"
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"

    #* Add matching labels to TRUE_LABELS for each new post.
    "mixed",     # "Lowkey stressed but kind of proud of myself"
    "positive",  # "Just had the best coffee ever! :)"
    "mixed",     # "This movie is so bad it's good"
    "positive",  # "Feeling like a million bucks today! 💰"
    "negative",  # "Why does everything have to be so hard?"
    "mixed",     # "I'm not sure how I feel about this..."
    "neutral",   # "Well, that was unexpected."
    "mixed",     # "I guess it could be worse."
    "positive",  # "I can't believe this happened! 😂"
    "mixed",     # "This is the best day ever... or is it? 🤔"
    "mixed",     # "I'm really not sure about this."
    "mixed",     # "This is kind of a mess, but also kind of fun."
    "mixed",     # "I absolutely love getting stuck in traffic"
    "mixed",     # "This is so bad, it's actually kind of amazing"
    "mixed"      # "I don't know whether to laugh or cry about this"
]

