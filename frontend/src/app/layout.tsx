import type { Metadata } from 'next';

// Commented out since globals.css was not found in your repository structure.
// If you add a globals.css file later, you can uncomment this line.
// import './globals.css'; 

export const metadata: Metadata = {
  title: 'EchoLogic AI Portal',
  description: 'AssemblyAI Voice Agent Real-Time Operations Environment',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased selection:bg-blue-500/30">
        {children}
      </body>
    </html>
  );
}
