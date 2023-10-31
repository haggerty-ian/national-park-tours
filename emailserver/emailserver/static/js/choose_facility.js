window.addEventListener('load', () => {
    let element = document.getElementById('facility-select')
    element.addEventListener('change', (event) => {
        console.log(event)
        event.target.parentElement.submit()
    })
})

