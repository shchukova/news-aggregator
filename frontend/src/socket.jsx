import { useRef, useState, useEffect } from 'react';
import { io } from "socket.io-client";

const SOCKET_URL = "http://127.0.0.1:5000";

const useSocket = () => {
    const [isConnected, setIsConnected] = useState(false);
    const [ddx, setDdx] = useState("");
    const [qa, setQa] = useState("");
    const socketRef = useRef(null);

    if (!socketRef.current) {
        socketRef.current = io(SOCKET_URL, { autoConnect: false });
    }

    useEffect(() => {
        const socket = socketRef.current;
        socket.on('connect', () => {
            console.log('Socket connected');
            setIsConnected(true);
        });

        socket.on('disconnect', () => {
            console.log('Socket disconnected');
            setIsConnected(false);
        });
        socket.on("cds_ddx", data => {
            console.log(data);
            setDdx(data.replaceAll("\n", "\n\n"));
        });

        socket.on("cds_qa", data => {
            console.log(data);
            setQa(data.replaceAll("\n", "\n\n"));
        });

        socket.connect();

        return () => {
            socket.off('connect');
            socket.off('disconnect');
            socket.off("cds_ddx");
            socket.off("cds_qa");
            socket.disconnect();
        };
    }, []);

    return { isConnected, ddx, qa, socket: socketRef.current };
};

export default useSocket;