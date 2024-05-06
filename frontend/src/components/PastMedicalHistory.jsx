import { MdMessage } from "react-icons/md";
import DigitalTwin from "./DigitalTwin";

const PastMedicalHistory = () => {
  return (
    <>
      <section className="max-w-[600px] m-2 bg-white rounded-lg">
        <h1 className="ml-10 pt-4 text-2xl font-extrabold text-black">
          Past Medical History
        </h1>
        <h1 className="ml-10">Relevant Match</h1>
        <div className="flex items-center ml-10">
          <MdMessage style={{ marginRight: "10px" }} color="gray" size={20} />
          <h1>Test Results</h1>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3 mt-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <div className="flex items-center ml-10">
          <MdMessage style={{ marginRight: "10px" }} color="gray" size={20} />
          <h1>Prescription</h1>
        </div>
        <h1 className="ml-10 mt-4">Timeline</h1>
        <div className="flex items-center ml-10">
          <MdMessage style={{ marginRight: "10px" }} color="gray" size={20} />
          <h1>AI Assessment</h1>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <div className="flex items-center ml-10">
          <MdMessage style={{ marginRight: "10px" }} color="gray" size={20} />
          <h1>AI Assessment</h1>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <div className="flex items-center ml-10">
          <MdMessage style={{ marginRight: "10px" }} color="gray" size={20} />
          <h1>Appointment</h1>
        </div>
        <div className="flex justify-between items-center mx-10 mb-3">
          <p className="bg-blue-300 rounded-lg">Normal(all)</p>
          <h6 className="text-gray-400">4 weeks ago</h6>
        </div>
        <button className="relative left-[86%] pb-2">See more</button>
      </section>
      <section className="bg-white max-w-[600px] max-h-screen m-2 rounded-lg pb-[110px]">
        <DigitalTwin />
      </section>
    </>
  );
};

export default PastMedicalHistory;
