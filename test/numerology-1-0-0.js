const numData = document.getElementById('data');

const first = document.getElementById('first');
const middle = document.getElementById('middle');
const last = document.getElementById('last');
const month = document.getElementById('month');
const day = document.getElementById('day');
const year = document.getElementById('year');
const submit = document.getElementById('submit');
const output = document.getElementById('output');

const vowel = ['A', 'E', 'I', 'O', 'U', 'Y']

let firstUp = first.toUpperCase();
let middleUp = middle.toUpperCase();
let lastUp = last.toUpperCase();

const fullName = firstUp + middleUp + lastUp;
const dob = month + day + year;

const currentDate = new Date().toJSON().slice(0, 10);
/* currYear = [0:4], currMon = [5:7], currDay = [8:] */

let fullNameArray = fullName.split("");
let dobArray = dob.split("").map(Number);

function addition(total, value, index, array) {
    return total + value;
}

function simplify(x) {
    if (x > 9) {
        let xStr = x.toString();
        let xArray = xStr.split("").map(Number);
        let xSimp = xArray.reduce(addition);
        return xSimp;
    }
}

function birthNum() {
    let birthArray = day.split("").map(Number);
    let birthNum = birthArray.reduce(addition);
    if (birthNum > 9) {
        let birthNum2 = simplify(birthNum);
        return birthNum2;
    } else {
        return birthNum;
    }
}

function lifePath() {
    let lifePath = dobArray.reduce(addition);
    if (lifePath > 9) {
        let lifePath2 = simplify(lifePath);
        if (lifePath2 > 9) {
            let lifePath3 = simplify(lifePath2);
            return lifePath3;
        } else {
        return lifePath2;
        }
    } else {
        return lifePath;
    }
}

function univYear() {
    let currYear = currentDate.slice(0, 4);
    let currYearArray = currYear.split("").map(Number);
    let univYear = currYearArray.reduce(addition);
    if (univYear > 9) {
        let univYear2 = simplify(univYear);
        if (univYear2 > 9) {
            let univYear3 = simplify(univYear2);
            return univYear3;
        } else {
            return univYear2;
        }
    } else {
        return univYear;
    }
}

function univMon() {
    let univY = univYear().toString();
    let currMon = currentDate.slice(5, 7);
    let currMonStr = univY + currMon;
    let currMonArray = currMonStr.split("").map(Number);
    let univMon = currMonArray.reduce(addition);
    if (univMon > 9) {
        let univMon2 = simplify(univMon);
        if (univMon2 > 9) {
            let univMon3 = simplify(univMon2);
            return univMon3;
        } else {
            return univMon2;
        }
    } else {
        return univMon;
    }
}

function persYear() {
    let pYear = month + day + currentDate.slice(0, 4);
    let persYearArray = pYear.split("").map(Number);
    let persYear = persYearArray.reduce(addition);
    if (persYear > 9) {
        let persYear2 = simplify(persYear);
        if (persYear2 > 9) {
            let persYear3 = simplify(persYear2);
            return persYear3;
        } else {
            return persYear2;
        }
    } else {
        return persYear;
    }
}

function persMon() {
    let persY = persYear().toString();
    let currMo = currentDate.slice(5, 7);
    let currMoStr = persY + currMo;
    let currMoArray = currMoStr.split("").map(Number);
    let persMo = currMoArray.reduce(addition);
    if (persMo > 9) {
        let persMon2 = simplify(persMo);
        if (persMon2 > 9) {
            let persMon3 = simplify(persMon2);
            return persMon3;
        } else {
            return persMon2;
        }
    } else {
        return persMo;
    }
}

function persDay() {
    let persMn = persMon().toString();
    let date = currentDate.slice(8, 10);
    let currDayStr = persMn + date;
    let currDayArray = currDayStr.split("").map(Number);
    let persD = currDayArray.reduce(addition);
    if (persD > 9) {
        let persD2 = simplify(persD);
        if (persD2 > 9) {
            let persD3 = simplify(persD2);
            return persD3;
        } else {
            return persD2;
        }
    } else {
        return persD;
    }
}

console.log(first + " " + middle + " " + last);
console.log(month + "/" + day + "/" + year + "\n");
console.log("Birth Number: " + birthNum());
console.log("Life Path Number: " + lifePath());
console.log("Universal Year: " + univYear());
console.log("Universal Month: " + univMon());
console.log("Personal Year: " + persYear());
console.log("Personal Month: " + persMon());
console.log("Personal Day: " + persDay());
