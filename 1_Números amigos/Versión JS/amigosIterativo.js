console.time('loop');
const start = Date.now();
var n=100000;
list=[];
var x = 0;
var y = 0;
var i=1;
while (i <= n) {
    var a=i;
    for (var j = 1; j < i; j++) {
        if(i%j==0){
            x+=j;
        }
    }
    b=x;
    if(a!=b){
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
        if(a>b){
            i=a;
        }else{
            i=b;
        }
    }
    x=0; 
    y=0;
    i++; //aumentamos el ciclo en uno
}
const end=Date.now();
console.timeEnd('loop');
const time= end - start;
const lista = document.getElementById('list');
const tiempo = document.getElementById('time');
list.forEach(item => {
    lista.innerHTML += '<li>'+item+'</li>'
});
tiempo.innerHTML+='Tiempo de ejecución: '+time+' ms.';
