import type { Metadata } from 'next';
import './globals.css'; // Ensure you have standard tailwind directives inside this file

export const metadata: Metadata = {
  title: 'EchoLogic AI Portal',
  description: 'AssemblyAI Voice Agent Real-Time Operations Environment',
};

export default function RootLayout({
  children,
  providedContext,
}: {
  children: React.ReactNode;
  providedContext?: any;
}) {
  return (
    <html lang="en">
      <body className="antialiased selection:bg-blue-500/30">
        {children}
      </body>
    </html>
  );
}
