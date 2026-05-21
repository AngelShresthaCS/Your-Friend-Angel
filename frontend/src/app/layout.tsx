export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className="bg-gray-100 text-gray-900 antialiased">
      <body className="min-h-full flex flex-col">{children}
      </body>
    </html>
  );
}
