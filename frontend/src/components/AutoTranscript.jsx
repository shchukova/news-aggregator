import { MdRecordVoiceOver } from "react-icons/md";

const AutoTranscript = () => {
  
  return (
    <section className="w-full h-full bg-white">
      <div className="flex justify-between items-center mx-4 pt-4">
        <div className="flex items-center">
          <MdRecordVoiceOver size={20} />
          <h1 className="text-xl font-bold ml-3">
            GP to Patient auto-transcript
          </h1>
        </div>
        <button>Stop</button>
      </div>
      <div className="flex flex-col mx-4">
        <h1 className="text-lg font-bold">Louise</h1>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut illum
          inventore ad aspernatur expedita? Numquam eius rerum architecto,
          pariatur consequatur animi tenetur maiores, consectetur sunt
          doloremque repellat, molestiae blanditiis! Eos.
        </p>
        <h1 className="text-lg font-bold">You</h1>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Aut illum
          inventore ad aspernatur expedita? Numquam eius rerum architecto,
          pariatur consequatur animi tenetur maiores, consectetur sunt
          doloremque repellat, molestiae blanditiis! Eos.
        </p>
      </div>
      <hr />
    </section>
  );
};

export default AutoTranscript;
