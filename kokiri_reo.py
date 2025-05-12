# kokiri_reo.py – Tennis Atmospheric Parser

def parse_tennis_commentary(line):
    line = line.lower()
    tags = []

    fire_phrases = [
        'dictating play',
        'winning all rallies',
        'looks unstoppable',
        'crushing returns',
        'breaking serve with ease',
        'playing with total control',
        'ripping forehands'
    ]

    suppression_phrases = [
        'can’t hold serve',
        'unforced errors piling',
        'double fault',
        'losing rhythm',
        'struggling to close',
        'losing composure'
    ]

    mist_phrases = [
        'momentum unclear',
        'match in balance',
        'long deuce',
        'neither player dominating',
        'swinging wildly',
        'both playing safe'
    ]

    for phrase in fire_phrases:
        if phrase in line:
            tags.append('fire')
    for phrase in suppression_phrases:
        if phrase in line:
            tags.append('suppression')
    for phrase in mist_phrases:
        if phrase in line:
            tags.append('mist')

    return tags

# Example usage
if __name__ == '__main__':
    example = "He’s losing rhythm and can’t hold serve right now"
    print(f"Tags: {parse_tennis_commentary(example)}")
