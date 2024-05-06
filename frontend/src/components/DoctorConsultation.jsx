const DoctorConsultation = () => {
  return (
    <section className="rounded-b-lg bg-white pt-4">
      <div className="flex flex-col">
        <h1 className="text-xl font-bold ml-4">Doctor Consultation Notes</h1>
        <textarea
          className="border rounded-lg px-4 mt-2 ml-2 outline-none w-ful h-[170px]"
          placeholder="Examination notes"
        />
      </div>
    </section>
  );
};

export default DoctorConsultation;
