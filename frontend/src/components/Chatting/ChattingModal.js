import React, { useEffect, useState } from 'react'
import RoomChatModal from './RoomChatModal';
import { io } from 'socket.io-client';

function ChattingModal() {
    const [buttonStatus, setButtonStatus] = useState(false);
    const [socketInstance, setSocketInstance] = useState("");
    const [loading, setLoading] = useState(false);


    useEffect(() => {
        if (buttonStatus) {
            let socket = io('http://127.0.0.1:5000/', {
                transports: ['websocket'],
                cors: {
                    origin: 'http://localhost:3000/'
                }
            });

            console.log(socket);

            setSocketInstance(socket);
            // socket.on('connect', (data) => {
            //     console.log(data);
            // });

            // setLoading(false);

            // socket.on('disconnect', (data) => {
            //     console.log(data);
            // });

            // return function cleanup() {
            //     socket.disconnect();
            // }

            return () => socket.close();
        }
    }, [buttonStatus]);

    return (
        <div>
            {buttonStatus ? (
                <div>
                    <button onClick={() => setButtonStatus(false)}>Turn chat off </button>
                    {/* {!loading && (
                        <RoomChatModal
                            socket={socketInstance}
                        />
                    )} */}
                </div>
            ) : (
                <button onClick={() => setButtonStatus(true)}>Turn chat on </button>
            )}
        </div>
    )
}

export default ChattingModal
