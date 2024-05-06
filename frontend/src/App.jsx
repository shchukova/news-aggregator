import React from 'react';
import Navbar from "./components/Navbar";
import PastMedicalHistory from "./components/PastMedicalHistory";
import Middle from "./pages/Middle";
import RightSide from "./pages/RightSide";
import { SocketProvider, useSocketContext } from './socket_context';

const MainContent = () => {
  const { isConnected } = useSocketContext();
  return (
    <>
      <Navbar />
      <Middle />
      <RightSide />
      <PastMedicalHistory />
      <div>
        Socket is {isConnected ? 'Connected' : 'Disconnected'}
      </div>
    </>
  );
};

function App() {
  return (
    <SocketProvider>
      <MainContent />
    </SocketProvider>
  );
}

export default App;