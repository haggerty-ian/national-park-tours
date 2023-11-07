window.addEventListener('load', () => {
    let elements = document.getElementsByTagName('select')
    elements.foreach(e => {
        e.addEventListener('change', (event) => {
            console.log(event)
            event.target.parentElement.submit()
        })
    })
})
