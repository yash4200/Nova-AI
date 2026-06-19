import "./VoiceCard.css";
import { useState } from "react";
import api from "../../services/api";

export default function VoiceCard() {

    const [listening, setListening] = useState(false);
    const [text, setText] = useState("");
    const [reply, setReply] = useState("");

    const startListening = () => {

        const SpeechRecognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!SpeechRecognition) {
            alert("Speech Recognition not supported");
            return;
        }

        const recognition = new SpeechRecognition();

        recognition.lang = "en-US";

        recognition.start();

        setListening(true);

        recognition.onresult = async (event) => {

            const transcript = event.results[0][0].transcript;

            setText(transcript);

            const res = await api.post("/ask", {

                text: transcript

            });

            setReply(res.data.response);

            const speech = new SpeechSynthesisUtterance(
                res.data.response
            );

            speech.lang = "en-US";

            window.speechSynthesis.speak(speech);

            setListening(false);

        };

        recognition.onerror = () => {

            setListening(false);

        };
    };

    return (

        <div className="voice-card">

            <h2>🎤 Nova Voice Assistant</h2>

            <button onClick={startListening}>

                {listening ? "Listening..." : "Start Listening"}

            </button>

            <h3>You Said</h3>

            <p>{text}</p>

            <h3>Nova</h3>

            <p>{reply}</p>

        </div>

    );

}