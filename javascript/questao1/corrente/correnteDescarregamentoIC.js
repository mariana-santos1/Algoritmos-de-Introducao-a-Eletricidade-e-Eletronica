let e = 12;
let r = 47000;
let c = 0.0022;
let neper = 2.71828;
let tal = r*c;
let t1 = tal/30;
let t = t1;
let cont = 1;

while (cont <= 30) {
    let ic = ((e/r) * (neper ** (-t/tal)));
    console.log(cont + ': ' + ic);
    t = t + t1;
    cont = cont + 1;
}