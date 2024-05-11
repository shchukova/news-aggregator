import { MdRecordVoiceOver } from "react-icons/md";
import { useSocketContext } from '../socket_context'; 
import React from 'react'
import ReactMarkdown from 'react-markdown'
const AutoTranscript = () => {
  const { transcript, isConnected, running } = useSocketContext();
  return (
    <section className="w-full h-full bg-white">
      <div className="flex justify-between items-center mx-4 pt-4">
        <div className="flex items-center">
          <MdRecordVoiceOver size={20} />
          <h1 className="text-xl font-bold ml-3">
            GP to Patient auto-transcript
          </h1>
        </div>
        {running &&  (
          <button className=
          {`${running ? 'animate-pulse bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 border-b-4 border-red-700 hover:border-red-500 rounded ' : ''}`}>
            Recording</button>  
        )}
        
      </div>
      <div className="flex flex-col mx-4">
        <h1 className="text-lg font-bold">Conversation Transcript:</h1>
        <div className="overflow-auto">
          {transcript ?
            <ReactMarkdown children={transcript} /> :
            <p className="text-gray-500">Waiting for transcript...</p>
          }
        </div>
        
      </div>
      <hr />
    </section>
  );
};

export default AutoTranscript;
