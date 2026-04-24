const check = document.getElementById("check").checked;
const output = document.getElementById("output");
const button = document.getElementById("button");
const sl = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
const ll = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
const sp = ["~", "@", "#", "$", "_", "-"]

function password () {
    let amount = document.getElementById("amount").value;
    let out = "";
    if (amount < 6) {
        amount = 6;
    }
    if (amount > 24) {
        amount = 24;
    }
    if (check)
        do {
            let number = Math.floor(Math.random() * 10);
            let number1 = Math.floor(Math.random() * 4);
            let number2 = Math.floor(Math.random() * 26);
            let number4 = Math.floor(Math.random() * 6);
            if (number1 == 0) {
                out += String(number);
                amount -= 1;
            }
            if (number1 == 1) {
                out += String(sl[number2]);
                amount -= 1;
            }
            if (number1 == 2) {
                out += String(ll[number2]);
                amount -= 1;
            }
            if (number1 == 3) {
                out += String(sp[number4]);
                amount -= 1;
            }
        }
        while (amount > -1);
    else {
        do {
            let number3 = Math.floor(Math.random() * 3);
            let number2 = Math.floor(Math.random() * 26);
            let number4 = Math.floor(Math.random() * 6);
            if (number3 == 1) {
                out += String(sl[number2]);
                amount -= 1;
            }
            if (number1 == 0) {
                out += String(ll[number2]);
                amount -= 1;
            }
            if (number1 == 2) {
                out += String(sp[number4]);
                amount -= 1;
            }
        }
        while (amount > -1);
    }
    output.style.width = (out.length * 25) + "px";
    output.value = out;
}

