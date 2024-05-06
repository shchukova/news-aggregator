import React from 'react';

import { useSocketContext } from '../socket_context'; 

const VideoCall = () => {
  const { isConnected, socket } = useSocketContext();
  const [running, setRunning] = React.useState(false);

  const startMic = () => {
    console.log("Emitting start_recording");
    console.log(isConnected)
    socket.emit("start_recording", { dummyData: "data" }, (value) => {
        console.log("Callback received with value:", value);
        if (value) {
            console.log("Setting running to true.");
            setRunning(true);
        }
    });
};

  const stopMic = () => {
    console.log("Emitting stop_recording");
    socket.emit("stop_recording", undefined, (value) => {
      console.log("Callback received with value:", value);
      if (value) {
        console.log("Setting running to false.");
        setRunning(false);
      }
    });
  };

  return (
    <section className="w-[400px] h-[400px] absolute bg-white mt-2 rounded-lg">
      <div>
        <h1>Video</h1>
        <div className="absolute bottom-0 right-0 h-14 w-16 left-[80%]">
          {isConnected ? (
            running ? (
              <button className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 border-b-4 border-red-700 hover:border-red-500 rounded" onClick={stopMic}>
                Stop
              </button>
            ) : (
              <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded" onClick={startMic}>
                start
              </button> 
            )
          ) : (
            <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-red-700 hover:border-red-500 rounded" onClick={stopMic} disabled>Not connected</button>
          )}
        </div>
        
      </div>
    </section>
  );
};

export default VideoCall;