const LivePossibleCauses = () => {
  return (
    <section className="mt-2 bg-white w-[400px] h-[260px] px-4 rounded-lg">
      <h1 className="text-xl font-bold mb-4">Live Possible Causes</h1>
      <div className="mb-3">
        <h1>Meniere disease</h1>
        <div className="w-full bg-gray-200 rounded-full h-1.5">
          <div
            className="bg-blue-600 h-1.5 rounded-full"
            style={{ width: "90%" }}
          ></div>
        </div>
        <h6 className="text-gray-400">90% Very Likely</h6>
      </div>
      <div className="mb-3">
        <h1>Benign Paroxysmal Positional Vertigo</h1>
        <div className="w-full bg-gray-200 rounded-full h-1.5">
          <div
            className="bg-blue-600 h-1.5 rounded-full"
            style={{ width: "10%" }}
          ></div>
        </div>
        <h6 className="text-gray-400">10% Less Likely</h6>
      </div>
      <div className="mb-3">
        <h1>Labyrinthistis</h1>
        <div className="w-full bg-gray-200 rounded-full h-1.5">
          <div
            className="bg-blue-600 h-1.5 rounded-full"
            style={{ width: "5%" }}
          ></div>
        </div>
        <h6 className="text-gray-400">5% Less Likely</h6>
      </div>
    </section>
  );
};

export default LivePossibleCauses;
