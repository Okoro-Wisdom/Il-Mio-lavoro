<svelte:head>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wgt,FILL,GRAND@48,400,0,0" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel ="stylesheet">
</svelte:head>
<script>
    import {createEventDispatcher} from "svelte";
    import {store_counter} from '../js/store.js';


    const dispatch = createEventDispatcher();
    export let counter = 0;
    function incrementa() {
      counter++;
      $store_counter = counter
      emit_event("incremento");
    }
    function decremento() {
      counter--;
      $store_counter = counter
      emit_event("decremento");
    }

    function emit_event(tipo){
        dispatch('contatore', {
            tipo:tipo,
            valore:counter
        })
    }
    
</script>

<div class="container">
    <div class="pulsante">
        <button on:click={decremento}>
            <span class="material-symbols-outlined icon">-</span>
        </button>
    </div>
    <div class="number">
        {$store_counter}   
    </div>
    <div class="pulsante">
        <button on:click={incrementa}>
            <span class="materiale-symbols-outlined icon">+</span>
        </button>
    </div>
</div>

<style>
    .container{
        border: 4px  solid #D43c2f;
        display: flex;
        justify-content: space-between;
        border-radius:  30px;
        width: 300px;
        padding: 10px;
        }
        .pulsante{
        display: flex;
        align-items: center;
        } 
        button{
        border: none;
        background: none;
        }
        .icon {
        font-size: 2.5rem;
        color: #f09c00;
        font-weight: bolder;
        }
        .icon:active{
        text-shadow: 1px 1px 10px #d43c2f;
        }
        .number{
        font-size: 4rem;
        font-family: 'Bungee Spice',cursive;
        }
</style>