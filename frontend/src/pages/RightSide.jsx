import AutoTranscript from "../components/AutoTranscript";
import ClinicalCodes from "../components/ClinicalCodes";
import DoctorConsultation from "../components/DoctorConsultation";

const RightSide = () => {
  return (
    <>
      <div className="absolute ml-[1040px] rounded-lg pr-2">
        <ClinicalCodes />
        <AutoTranscript />
        <DoctorConsultation />
      </div>
    </>
  );
};

export default RightSide;
