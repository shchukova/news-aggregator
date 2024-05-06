import human from "../assets/human.png";

const DigitalTwin = () => {
  return (
    <section>
      <div className="ml-10">
        <h1>Digital Twin</h1>
      </div>
      <img
        className="ml-[350px]"
        style={{ width: "100px" }}
        src={human}
        alt=""
      />
    </section>
  );
};

export default DigitalTwin;
