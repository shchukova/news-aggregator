import React, { createContext, useContext } from 'react';
import useSocket from './socket';  

const SocketContext = createContext(null);

export const SocketProvider = ({ children }) => {
    const socket = useSocket();
    return <SocketContext.Provider value={socket}>{children}</SocketContext.Provider>;
};

export const useSocketContext = () => useContext(SocketContext);