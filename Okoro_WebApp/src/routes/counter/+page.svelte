
<script>
   import Counter from "$lib/components/counter.svelte";
   import DoubleCounter from "$lib/components/dueblecounter.svelte";
   
   function gestisci_evento(evento){
      alert(`${evento.detail.tipo} -- ${evento.detail.valore}`)
   }

    let contatore = 0
    let contatore2 = 0
    let numeri = [1,7,3,5,9,0]
    let sottolinea = true;
    let doppio;
    $: doppio = contatore *2

</script>

<h1>Pagina Counter !!</h1>
<h2 class:sottolinea>Il valore del contatore vale {contatore}</h2>
<h3 class:sottolinea>Il Valore del contatore doppio vale : {doppio} </h3>
<Counter bind:counter={contatore} on:contatore={gestisci_evento}/>
<DoubleCounter bind:counter={contatore2}/>

<ul>
  {#each numeri as numero ,indice}
  <li>numeri[{indice}]:{numero}</li>
  {/each}
</ul>
<style>
    .sottolinea {
      text-decoration: underline;
      color: rgb(6, 97, 182);
      }
</style>