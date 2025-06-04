function test_comms() {
    fetch("http://localhost:8000/api/test")
        .then(res => res.text())
        .then(data => console.log(data))
}