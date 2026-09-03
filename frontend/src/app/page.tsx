import VoiceInterface from '@/components/VoiceInterface';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-6 bg-slate-950 text-white">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex flex-col">
        <header className="w-full text-center border-b border-slate-800 pb-6 pt-8 backdrop-blur-2xl">
          <h1 className="text-4xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">
            EchoLogic AI Portal
          </h1>
          <p className="mt-2 text-slate-400">AssemblyAI Voice Agent Real-Time Operations Environment</p>
        </header>

        <div className="flex flex-col items-center justify-center w-full my-auto py-12">
          <VoiceInterface />
        </div>

        <footer className="w-full text-center text-xs text-slate-600 border-t border-slate-900 pt-4">
          EchoLogic AI Architecture • Built for lablab.ai Hackathon
        </footer>
      </div>
    </main>
  );
}
