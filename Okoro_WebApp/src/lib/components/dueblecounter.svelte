<svelte:head>
  <link href="https://fonts.googleleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" rel=stylesheet/>
  <link href="https://fonts.googleleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet"/>
</svelte:head>

<script>
    import {createEventDispatcher} from "svelte";
    import {store_double_counter} from '../js/store.js';


    const dispatch = createEventDispatcher();

    export let counter = 0;
  
    function incrementa() {
      counter += 2 ;
      $store_double_counter = counter
    }

    function decrementa() {
      $store_double_counter = counter
      counter -= 2;
    }
  </script>
<h2>Counter 2</h2>
<div class="container">
    <div class="pulsante">
        <button on:click={decrementa}>
            <span class="materiale-symbols-outline icon">-</span>
        </button>
    </div>
    <div class="number">
        {$store_double_counter}
    </div>
    <div class="pulsante">
        <button on:click={incrementa}>
            <span class="materiale-symbols-outline icon">+</span>
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