// Inicia cuenta del tiempo: toma valor inicial
console.time('loop')
const start = Date.now()

// Crea un arreglo vacio
let list=[]

// funcion para obtener los divisores de un numero i
function divisores(i,j){
    if(j<2){
        return j;
    }else if(i%j===0){
        return j+divisores(i,j-1)
    }else{
        return divisores(i,j-1)
    }
}

// El cálculo de max determina un rango donde todos sus posibles divisores de encuentran
// por ejemplo, para el numero 100 todos sus divisores de acumulan en el rango [1,50] 
// después del 50 no se encuentran más divisores candidatos.
// Otro ejemplo, si el numero es el 99, sus divisores se encontrarán entre el [1,33]

// funcion para determinar los numeros amigos en un rango de valores [1 hasta i]
function amigo(i,arreglo){
    if(i>1){
        let x=i
        // Calculo para determinar max
            let max = 0;
            if(i%2==0) {
                max=Math.trunc((i/2)+1);
            }
            else if(i%3==0) {
                max=Math.trunc((i/3)+1);
            }else if(i%5==0) {
                max=Math.trunc((i/5)+1);
            }else if(i%7==0) {
                max=Math.trunc((i/7)+1);
            } else if(i%11==0) {
                max=Math.trunc((i/11)+1);
            }
        // fin calculo para determinar max
        let y=divisores(x, max);
        if(y<x){
            // Calculo para determinar max
                let max2 = 0;
                if(y%2==0) {
                    max2=Math.trunc((y/2)+1);
                }
                else if(y%3==0) {
                    max2=Math.trunc((y/3)+1);
                }else if(y%5==0) {
                    max2=Math.trunc((y/5)+1);
                }else if(y%7==0) {
                    max2=Math.trunc((y/7)+1);
                } else if(y%11==0) {
                    max2=Math.trunc((y/11)+1);
                }
            // fin calculo para determinar max
            a=divisores(y,max2)
            if(a===x){
                arreglo.push([x,y]);
            }
        }
        return amigo(i-1,arreglo)
    }else{
        return arreglo
    }
}


let amigos = amigo(100000,list)   // ====> el maximo valor de i posible en la pila de recursion soportado por javascript en un I7 8va gen con 16gb ram es 8920

// Finaliza conteo del tiempo; Compara inicial y final para determinar tiempo total
const end=Date.now();
console.timeEnd('loop');
const time= end - start;
console.log('Rango evaluado: 100000')
// Vista de valores en consola
console.log('Tiempo de ejecucion:'+time+'ms')
console.log(amigos)


// vista de valores por front
// const lista = document.getElementById('list');
// const tiempo = document.getElementById('time');
// list.forEach(item => {
//     lista.innerHTML += '<li>'+item+'</li>'
// });
// tiempo.innerHTML+='Tiempo de ejecución: '+time+' ms.';
