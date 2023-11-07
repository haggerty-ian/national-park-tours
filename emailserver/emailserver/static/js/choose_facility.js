window.addEventListener('load', () => {
    let elements = document.getElementsByTagName('select')
    elements.addEventListener('change', (event) => {
        console.log(event)
        event.target.parentElement.submit()
    })
})
