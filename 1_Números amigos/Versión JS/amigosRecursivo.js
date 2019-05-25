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

// funcion para determinar los numeros amigos en un rango de valores [1 hasta i]
function amigo(i,arreglo){
    if(i>1){
        let x=i
        let z= Math.trunc((i/2)+1);
        let y=divisores(x,z)
        if(y<x){
            a=divisores(y,y-1)
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
