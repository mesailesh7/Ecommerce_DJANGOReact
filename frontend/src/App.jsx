import {useEffect, useState} from "react";

import React from 'react'

const App = () => {
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error fetching message', error))
    }, []);

    console.log(message)
    return (
        <>
            <h1>Message from backend</h1>
            <div>{message || 'Loading...'}</div>
        </>
    )
}
export default App
