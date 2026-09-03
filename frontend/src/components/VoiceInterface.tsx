'use client';

import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Radio, Server } from 'lucide-react';

export default function VoiceInterface() {
  const [isConnected, setIsConnected] = useState<boolean>(false);
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [agentStatus, setAgentStatus] = useState<string>('Disconnected');
  const socketRef = useRef<WebSocket | null>(null);

  // Initialize secure pipeline connection to AssemblyAI Voice Agent Interface
  const toggleVoiceSession = async () => {
    if (isConnected) {
      if (socketRef.current) socketRef.current.close();
      setIsConnected(false);
      setIsRecording(false);
      setAgentStatus('Disconnected');
    } else {
      setAgentStatus('Connecting to AssemblyAI Layer...');
      try {
        // Fetch ephemeral connection tokens secure from serverless environment
        // Replace with your route or direct development credentials safely 
        const mockTargetWS = "wss://://assemblyai.com";
        
        // In local/production development, plug the AssemblyAI streaming layer here
        setIsConnected(true);
        setIsRecording(true);
        setAgentStatus('Streaming Active (Listening)');
      } catch (err) {
        setAgentStatus('Connection pipeline failed');
        setIsConnected(false);
      }
    }
  };

  return (
    <div className="w-full max-w-md p-6 bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl flex flex-col items-center space-y-6">
      <div className="flex items-center justify-between w-full border-b border-slate-800 pb-3">
        <div className="flex items-center space-x-2">
          <Server className="text-blue-400 w-5 h-5" />
          <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Vercel Edge Gateway</span>
        </div>
        <div className="flex items-center space-x-1.5">
          <span className={`w-2.5 h-2.5 rounded-full ${isConnected ? 'bg-emerald-500 animate-pulse' : 'bg-rose-500'}`} />
          <span className="text-xs text-slate-300 font-medium">{agentStatus}</span>
        </div>
      </div>

      <button
        onClick={toggleVoiceSession}
        className={`w-32 h-32 rounded-full flex flex-col items-center justify-center transition-all duration-300 transform active:scale-95 shadow-lg ${
          isRecording 
            ? 'bg-rose-600 hover:bg-rose-500 shadow-rose-900/40 text-white' 
            : 'bg-blue-600 hover:bg-blue-500 shadow-blue-900/40 text-white'
        }`}
      >
        {isRecording ? <MicOff className="w-12 h-12" /> : <Mic className="w-12 h-12" />}
        <span className="text-xs font-bold mt-2 uppercase tracking-wide">
          {isRecording ? 'Mute Session' : 'Start Agent'}
        </span>
      </button>

      <div className="w-full bg-slate-950 rounded-xl p-4 border border-slate-850 min-h-[80px] flex items-center justify-center">
        {isRecording ? (
          <div className="flex items-center space-x-1 text-blue-400">
            <Radio className="animate-spin w-4 h-4 mr-1" />
            <span className="text-xs animate-pulse font-mono">Listening for turn-taking voice actions...</span>
          </div>
        ) : (
          <p className="text-xs text-slate-500 text-center font-mono">Click button above to engage voice workspace infrastructure.</p>
        )}
      </div>
    </div>
  );
}
