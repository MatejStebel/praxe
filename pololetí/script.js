const input = document.getElementById("letters");
const button = document.getElementById("button");
const results = document.getElementById("output");

let dictionary = [];

function canBuildWord(word, letters) {
    const counts = {};

    for (const l of letters) {
    counts[l] = (counts[l] || 0) + 1;
    }

    for (const l of word) {
    if (!counts[l]) return false;
    counts[l]--;
    }

    return true;
}


fetch("words.txt")
    .then(res => res.text())
    .then(text => {
        dictionary = text
        .split("\n")
        .map(w => w.trim().toLowerCase())
        .filter(w => w.length > 0);
    });

    button.addEventListener("click", () => {
        const letters = input.value.toLowerCase().trim();
    const length = letters.length;

  results.innerHTML = ""; // clear old results

    if (length === 0) return;

    const matches = dictionary.filter(word =>
        word.length === length &&
        canBuildWord(word, letters)
        );


    matches.forEach(word => {
    const li = document.createElement("li");
    li.textContent = word;
    results.appendChild(li);
    });
});
