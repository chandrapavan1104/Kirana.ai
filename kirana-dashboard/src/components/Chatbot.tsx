import { useState, useRef, useEffect } from "react";
import { useCart } from '../context/cartContext'; // Import useCart

interface ChatMessage {
  sender: "user" | "system";
  text: string;
}

const Chatbot = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [recording, setRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const chatRef = useRef<HTMLDivElement>(null);

  const { addToCart } = useCart(); // Use the hook to get addToCart

  // Function to auto-scroll chat to latest message
  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }, [messages]);

  // Function to handle text command submission
  const sendTextCommand = async () => {
    if (!input.trim()) return;

    const userMessage: ChatMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch("http://localhost:8000/text-command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command: input }),
      });

      const data = await response.json();
      
      // Display the response message
      const systemMessageText = data.response || "⚠️ Error processing command.";
      const systemMessage: ChatMessage = { sender: "system", text: systemMessageText };
      setMessages((prev) => [...prev, systemMessage]);

      // Handle cart updates only if it's a successful add operation
      if (data.success && data.item && data.item.operation === 'add') {
        const addedItem = data.item;
        addToCart({
          id: addedItem.id,
          name: addedItem.name,
          quantity: addedItem.quantity_added,
          unit: addedItem.unit,
          price: addedItem.price,
        });
      }

    } catch (error) {
      console.error('Error:', error);
      setMessages((prev) => [...prev, { sender: "system", text: "⚠️ Error: Unable to process command." }]);
    }

    setInput("");
  };

  // Function to handle voice command
  const recordVoiceCommand = () => {
    navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
      const mediaRecorder = new MediaRecorder(stream);
      const audioChunks: Blob[] = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = async () => {
        setRecording(false);
        setIsProcessing(true);
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
        const formData = new FormData();
        formData.append("file", audioBlob, "command.wav");

        try {
          const res = await fetch("http://localhost:8000/transcribe", {
            method: "POST",
            body: formData,
          });
          const data = await res.json();
          setIsProcessing(false);

          if (data.transcription) {
            const userMessage: ChatMessage = { sender: "user", text: `🎤 ${data.transcription}` };
            setMessages((prev) => [...prev, userMessage]);

            // Send the transcribed text as a command
            const commandResponse = await fetch("http://localhost:8000/text-command", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ command: data.transcription }),
            });
            const commandData = await commandResponse.json();

            // Display the response message
            const systemMessageText = commandData.response || "⚠️ Error processing command.";
            const systemMessage: ChatMessage = { sender: "system", text: systemMessageText };
            setMessages((prev) => [...prev, systemMessage]);

            // Handle cart updates only if it's a successful add operation
            if (commandData.success && commandData.item && commandData.item.operation === 'add') {
              const addedItem = commandData.item;
              addToCart({
                id: addedItem.id,
                name: addedItem.name,
                quantity: addedItem.quantity_added,
                unit: addedItem.unit,
                price: addedItem.price,
              });
            }
          } else {
            setMessages((prev) => [...prev, { sender: "system", text: "⚠️ Transcription failed." }]);
          }
        } catch (err) {
          console.error('Error:', err);
          setIsProcessing(false);
          setMessages((prev) => [...prev, { sender: "system", text: "⚠️ Voice command failed." }]);
        }
      };

      mediaRecorder.start();
      setRecording(true);
      (window as any)._mediaRecorder = mediaRecorder;
    });
  };

  // Cancel/stop recording
  const cancelRecording = () => {
    if ((window as any)._mediaRecorder) {
      (window as any)._mediaRecorder.stop();
      setRecording(false);
    }
  };

  // Function to send transcribed text as a command (This function is no longer directly called by voice command flow)
  // Keeping it for potential future use or if text command logic is reused.
  const sendTextCommandFromVoice = async (voiceText: string) => {
    const userMessage: ChatMessage = { sender: "user", text: `🎤 ${voiceText}` };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch("http://localhost:8000/process_command", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command: voiceText }),
      });

      const data = await response.json();
      const systemMessage: ChatMessage = { sender: "system", text: data.response || "⚠️ Error processing command." };
      setMessages((prev) => [...prev, systemMessage]);
    } catch (error) {
      setMessages((prev) => [...prev, { sender: "system", text: "⚠️ Error: Unable to process command." }]);
    }
  };

  return (
    <div className="w-full lg:w h-screen flex flex-col border-l border-gray-300 bg-white shadow-lg">
      {/* Chat Header */}
      <h2 className="text-2xl font-bold text-center py-4 border-b">🛒 Kirana Chatbot</h2>

      {/* Chat Messages */}
      <div ref={chatRef} className="flex-1 overflow-y-auto px-4 py-2 bg-gray-100 flex flex-col">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`my-1 rounded-lg w-full ${
              msg.sender === "user"
                ? "bg-blue-200"
                : "bg-green-200"
            }`}
            style={{ maxWidth: "100%" }}
          >
            <div className={`p-2 break-words ${msg.sender === "user" ? "text-end" : "text-start"}`}>
              {typeof msg.text === 'string' 
                ? msg.text.split('\n').map((line, i) => (
                    <div key={i}>{line}</div>
                  ))
                : <div>{String(msg.text)}</div>
              }
            </div>
          </div>
        ))}
      </div>

      {/* Input Field & Buttons */}
      <div className="p-4 flex gap-3 border-t">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a command..."
          className="flex-grow p-2 border rounded-lg"
          disabled={isProcessing}
        />
        <button onClick={sendTextCommand} className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600" disabled={isProcessing}>
          Send
        </button>
        {!recording && !isProcessing && (
          <button
            onClick={recordVoiceCommand}
            className="px-4 py-2 rounded-lg text-white bg-red-500 hover:bg-red-600"
            disabled={isProcessing}
          >
            🎤
          </button>
        )}
        {recording && (
          <button
            onClick={cancelRecording}
            className="px-4 py-2 rounded-lg text-white bg-gray-700 hover:bg-gray-900"
          >
            ❌
          </button>
        )}
        {isProcessing && (
          <button
            className="px-4 py-2 rounded-lg text-white bg-gray-400 cursor-not-allowed"
            disabled
          >
            ⏳
          </button>
        )}
      </div>
    </div>
  );
};

export default Chatbot;
