import type { NextPage } from "next";
import AudioRecorder from "../components/AudioRecorder";

const Home: NextPage = () => {
  return (
    <div className="bg-slate-700 text-white px-10 py-32 min-h-screen flex flex-col justify-start items-center space-y-5">
      <h1 className="text-2xl font-extrabold mb-32">AI Assistant</h1>
      <AudioRecorder />
    </div>
  );
};

export default Home;
