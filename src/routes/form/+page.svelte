<script>
    let input1 = '';
    let input2 = '';
    let input3 = '';
</script>

<main>
    <form>
        <div>
            <label for="input1">Input 1:</label>
            <input type="text" id="input1" bind:value={input1} />
        </div>
        <div>
            <label for="input2">Input 2:</label>
            <input type="text" id="input2" bind:value={input2} />
        </div>
        <div>
            <label for="input3">Input 3:</label>
            <input type="text" id="input3" bind:value={input3} />
        </div>
        <button type="submit">Submit</button>
    </form>
</main>

<style>
    main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
</style>