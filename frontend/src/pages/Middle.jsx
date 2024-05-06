import LivePossibleCauses from "../components/LivePossibleCauses";
import SuggestedQuestions from "../components/SuggestedQuestions";
import VideoCall from "../components/VideoCall";

const Middle = () => {
  return (
    <>
      <div className="absolute mx-[630px] rounded-lg">
        <VideoCall />
        <SuggestedQuestions />
        <LivePossibleCauses />
      </div>
    </>
  );
};

export default Middle;
