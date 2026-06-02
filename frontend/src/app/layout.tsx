import "./globals.css";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="antialiased">
      <body className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(255,214,170,0.22),_transparent_40%),linear-gradient(180deg,_#fffaf3_0%,_#f2ece4_100%)] text-gray-900">
        {children}
      </body>
    </html>
  );
}
