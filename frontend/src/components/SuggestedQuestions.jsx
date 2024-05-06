import React from 'react'
import useSocket from '../socket';
import ReactMarkdown from 'react-markdown'
import { useSocketContext } from '../socket_context'; 

const SuggestedQuestions = () => {
  const { qa } = useSocketContext();
  return (
    <section className="mt-[415px] max-w-[400px] bg-white rounded-lg w-full h-full">
      <h1 className="text-xl font-bold ml-4">Suggested questions</h1>
      {/*<h6 className="ml-4 mt-3">Have you injured your ear recently?</h6> */}
      <div className="px-3">
        <ReactMarkdown>{qa}</ReactMarkdown>
      </div>
      
      <button className="relative left-[80%] pt-10">See more</button>
    </section>
  );
};

export default SuggestedQuestions;
