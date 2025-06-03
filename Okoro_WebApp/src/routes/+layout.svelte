<main>
    <header>
        <h1>The Honored One</h1>
    </header>

    <section>
        <nav>
            <ul>
                <li><a href="/chi_sono">Chi sono</a></li>
                <li><a href="/1_anno">I anno</a></li>
                <li><a href="/2_anno">II anno</a></li>
                <li><a href="/3_anno">III anno</a></li>
                <li><a href="/4_anno">IV anno</a></li>
                <li><a href="/5_anno">V anno</a></li>
            </ul>
        </nav>
        
        <article>
            <!--<p>Main content goes here</p>-->
            <slot />
        </article>

    </section>

    <footer>
        <h4>Creazione 11/03/2024 </h4>
    </footer>

</main>

<style>
    :global(body){
        margin: 0%;
    }
    main{
        display: flex;
        flex-direction: column;
        height: 100vh;
        box-sizing:  border-box;
        color: white;
    }
    header{
        background-color: #023e8a;
        text-align: center;
    }
    section{
        display: flex;
        flex-direction: row;
        flex: 10;
    }
    nav{
        background-color: #0077b6;
        flex: 1;
    }
    nav ul{
        list-style: none;
    }
    nav ul li{
        padding: 10px;
    }
    nav ul li a{
        color: white;
        text-decoration: none;
        font-size: 30px;
        font-weight: bolder;
    }

    article{
        color: #03045e;
        padding: 20px;
        font-size: 30px;
        flex: 8;
        
    }
    footer{
        background-color: #03045e;
        text-align: center;
        font-size: 10px;
        flex: 1;
    }
</style>