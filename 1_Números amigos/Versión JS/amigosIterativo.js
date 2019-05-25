console.time('loop');
const start = Date.now();
var n=1000000;
list=[];
var x = 0;
var y = 0;
for (var i = 1; i <= n; i++) {
    var a=i;
    for (var j = 1; j < i; j++) {
        if(i%j==0){
            x+=j;
        }
    }
    b=x;
    if(a>b){
        for(var k=1; k<b; k++){
            if(b%k==0){
                y+=k;
            }
        }
    }
    if(a==y){
        list.push(a+' es amigo de '+b);
    }
    x=0; y=0;
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
