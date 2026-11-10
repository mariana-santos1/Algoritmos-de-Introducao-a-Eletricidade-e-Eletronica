let e = 12;
let r = 470;
let l = 0.01;
let neper = 2.71828;
let tal = l/r;
let t1 = tal/30;
let t = t1;
let cont = 1;

while (cont <= 30) {
    let il = (e/r) * (neper ** (-t/tal));
    console.log(cont + ': ' + il);
    t = t + t1;
    cont = cont + 1;
}