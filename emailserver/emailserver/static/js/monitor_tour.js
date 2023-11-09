window.addEventListener('load', () => {
    let elements = document.getElementsByTagName('select')
    for (let e of elements) {
        e.addEventListener('change', (event) => {
            console.log(event)
            event.target.parentElement.submit()
        })
    }
})
