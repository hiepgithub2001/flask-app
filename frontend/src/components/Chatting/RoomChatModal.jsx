import React, { useEffect, useState } from 'react'

function RoomChatModal(props) {
    const { socket } = props;
    const [message, setMessage] = useState('')
    const [messages, setMessages] = useState([])

    const handleText = (e) => {
        setMessage(e.target.value)
    }

    const handleSubmit = () => {
        if (!message) {
            return;
        }

        socket.emit('data', message)
        setMessage('')
    }


    useEffect(() => {
        socket.on('data', (data) => {
            setMessages([...messages, data])
        });

        return () => {
            socket.off('data', () => {
                console.log('data event was removed!');
            });
        }
    }, [messages, socket]);


    return (
        <div>
            <h2> Web Socket communication </h2>
            <input type='text' onChange={handleText} value={message} />
            <button onClick={handleSubmit}> Submit </button>

            <ul>
                {messages.map((msg, index) => {
                    return <li key={index}> {msg} </li>
                })}
            </ul>
        </div>
    )
}

export default RoomChatModal
