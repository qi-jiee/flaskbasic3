from flask import Flask, render_template


app = Flask(__name__)

house_points = {"artemis": 3,
          "helios": 6767,
          "athena": 1,
          "poseidon": 0}

house_colours = {"artemis": "green",
                 "helios": "red",
                 "athena": "purple",
                 "poseidon": "blue"}

past_words = []
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<text>")
def info(text):
    if text in house_points.keys():
        house_color = house_colours[text]
        house_pt = house_points[text]
        return render_template("house.html", house=text, house_color=house_color, house_pt=house_pt)
    else:
        len_text = len(text)
        consonant_count = 0
        vowel_count = 0
        letter_freq = {}
        for char in text:
            if char.isalpha(): # check for alphabetical chars
                # vowel/consonant check
                if char in "AEIOUaeiou":
                    vowel_count += 1
                else:
                    consonant_count += 1
                char = char.lower()
                # add to frequency dict
                if char not in letter_freq.keys():
                    letter_freq[char] = 1
                else:
                    letter_freq[char] += 1
        past_words.append(text)
        return render_template("analysis.html", text=text, len_text=len_text, vowel_count=vowel_count, consonant_count=consonant_count, letter_freq=letter_freq, past_words=past_words)
if __name__ == "__main__":
    app.run(port=5555)
