console.time('loop');
const start = Date.now();
var n=100000;
list=[];
var x = 0; //almacena la sumatoria de divisores del primer valor
var y = 0;
var i=1;
while (i <= n) {
    
    //almaceno en a el valor actual de i que es el número que estoy analizando
    var a=i; //para i=220 => a=220
    //Hallo la sumatoria de divisores del numero i que es el numero que estoy analizando
    //y lo almaceno en x.
    for (var j = 1; j < i; j++) {
        if(i%j==0){
            x+=j;
        }
    }
    //x tendrá el valor de la sumatoria de i.
    b=x;
    //para i=220 => a=220 => x=248 => b=248
    if(a!=b){
        //Calcula la sumatoria de divisores de B que anteriormente se le almacenó la sumatoria de divisores de i
        for(var k=1; k<b; k++){
            if(b%k==0){
                y+=k;
            }
        }
    }

    if(a==y){
        list.push([a,b]);
        // si existe un numero amigo a la variable i que controla el ciclo principal le pasamos el numero amigo mayor para evitar 
        // controlar numeros amigos repetidos
        // console.log(i);
        if(a>b){
            i=a;
            console.log('nuevo valor de i',a)
        }else{
            i=b; 
            console.log('nuevo valor de i',b)
        }
    }
    x=0; 
    y=0;
    i++; //aumentamos el ciclo en uno
}
const end=Date.now();
console.timeEnd('loop');
console.log(list)
// const time= end - start;
// const lista = document.getElementById('list');
// const tiempo = document.getElementById('time');
// list.forEach(item => {
//     lista.innerHTML += '<li>'+item+'</li>'
// });
// tiempo.innerHTML+='Tiempo de ejecución: '+time+' ms.';
