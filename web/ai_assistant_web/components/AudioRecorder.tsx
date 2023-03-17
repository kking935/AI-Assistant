import { useState, useRef } from "react";

const AudioRecorder = () => {
  const [permission, setPermission] = useState(false);
  const mediaRecorder = useRef<MediaRecorder>();
  const [recordingStatus, setRecordingStatus] = useState("inactive");
  const [audioChunks, setAudioChunks] = useState([]);
  const [audio, setAudio] = useState<string>("");
  const [stream, setStream] = useState<MediaStream>();

  const getMicrophonePermission = async () => {
    if ("MediaRecorder" in window) {
      try {
        const streamData = await navigator.mediaDevices.getUserMedia({
          audio: true,
          video: false,
        });
        setPermission(true);
        setStream(streamData);
      } catch (err: any) {
        alert(err.message);
      }
    } else {
      alert("The MediaRecorder API is not supported in your browser.");
    }
  };

  const startRecording = async () => {
    setRecordingStatus("recording");
    //create new Media recorder instance using the stream
    const media = new MediaRecorder(stream as MediaStream, {
      mimeType: "audio/webm",
    });
    //set the MediaRecorder instance to the mediaRecorder ref
    mediaRecorder.current = media;
    //invokes the start method to start the recording process
    mediaRecorder.current.start();
    let localAudioChunks: any = [];
    mediaRecorder.current.ondataavailable = (event) => {
      if (typeof event.data === "undefined") return;
      if (event.data.size === 0) return;
      localAudioChunks.push(event.data);
    };
    setAudioChunks(localAudioChunks);
  };

  const stopRecording = () => {
    setRecordingStatus("inactive");
    //stops the recording instance
    if (!mediaRecorder || !mediaRecorder.current) return;
    mediaRecorder.current.stop();
    mediaRecorder.current.onstop = () => {
      //creates a blob file from the audiochunks data
      const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
      //creates a playable URL from the blob file.
      const audioUrl = URL.createObjectURL(audioBlob);
      console.log(audioUrl);
      setAudio(audioUrl);
      setAudioChunks([]);
    };
  };

  const submitAudio = () => {
    console.log(audio);
  };

  return (
    <>
      <div className="audio-controls">
        {!permission ? (
          <button
            className="p-3 rounded bg-blue-500 font-semibold"
            onClick={getMicrophonePermission}
            type="button"
          >
            Get Microphone
          </button>
        ) : null}
        {permission && recordingStatus === "inactive" ? (
          <button
            className="p-3 rounded bg-green-500 font-semibold"
            onClick={startRecording}
            type="button"
          >
            Start Recording
          </button>
        ) : null}
        {recordingStatus === "recording" ? (
          <button
            className="p-3 rounded bg-red-500 font-semibold"
            onClick={stopRecording}
            type="button"
          >
            Stop Recording
          </button>
        ) : null}
      </div>
      {audio ? (
        <div className="pt-32 flex flex-col space-y-3 items-center justify-center">
          <audio src={audio} controls></audio>
          <a
            className="p-3 rounded bg-yellow-500 font-semibold"
            download
            href={audio}
          >
            Download Recording
          </a>
          <button
            className="p-3 rounded bg-orange-500 font-semibold"
            onClick={submitAudio}
          >
            Submit Recording
          </button>
        </div>
      ) : null}
    </>
  );
};
export default AudioRecorder;
