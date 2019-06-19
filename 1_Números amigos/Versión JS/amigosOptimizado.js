// funcion para hallar divisores optimizando un valor maximo para numeros mayores a 50
function divisores(nro){
    let sumdiv = 0
    let max = nro;
    if(max>50){
        max = 0;
        if(nro%2==0) {
            max=Math.trunc((nro/2)+1);
        }
        else if(nro%3==0) {
            max=Math.trunc((nro/3)+1);
        }else if(nro%5==0) {
            max=Math.trunc((nro/5)+1);
        }else if(nro%7==0) {
            max=Math.trunc((nro/7)+1);
        } else if(nro%11==0) {
            max=Math.trunc((nro/11)+1);
        }
    }

    for (let i = 1; i < max; i++) {
        if(nro%i===0){
            sumdiv+=i
        }
    }
    return sumdiv
}

console.time('loop');
const start = Date.now();
var n=100000;
list=[];
var x = 0; //almacena la sumatoria de divisores del primer valor
var y = 0;

for (let j = 220; j < n; j++) {
 
    //almaceno en a el valor actual de i que es el número que estoy analizando
    var a=j; //para i=220 => a=220
    //Hallo la sumatoria de divisores del numero i que es el numero que estoy analizando
    //y lo almaceno en x.
    x=divisores(a)
    //x tendrá el valor de la sumatoria de i.
    b=x;
    //para i=220 => a=220 => x=248 => b=248
    if(a>b){
        //Calcula la sumatoria de divisores de B que anteriormente se le almacenó la sumatoria de divisores de i
        y=divisores(b)
    }

    if(a===y){
        list.push([b,a]);
        // si existe un numero amigo a la variable i que controla el ciclo principal le pasamos el numero amigo mayor para evitar 
        // controlar numeros amigos repetidos
        // console.log(i);
        // /* if(a>b){
        //     i=a;
        //     console.log('nuevo valor de i',a)
        // }else{
        //     i=b; 
        //     console.log('nuevo valor de i',b)
        // } */
    }
    x=0; 
    y=0;
}
const end=Date.now();
console.timeEnd('loop');
console.log(list)
const time= end - start;
// const lista = document.getElementById('list');
// const tiempo = document.getElementById('time');
// list.forEach(item => {
//     lista.innerHTML += '<li>'+item+'</li>'
// });
// tiempo.innerHTML+='Tiempo de ejecución: '+time+' ms.';