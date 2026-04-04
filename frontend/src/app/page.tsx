import Image from "next/image";// 1. Define the TypeScript interface to enforce the law on what Python returns
interface ApiStatus {
  status: string;
  value: string;
}
const res = await fetch("http://127.0.0.1:8000/", {
    // Next.js caches everything aggressively. This forces it to ask Python 
    // for a fresh status every single time you refresh the page.
    cache: "no-store", 
  });
//parse the JSON response from Python and enforce the structure defined by the ApiStatus interface
const data: ApiStatus = await res.json();

export default function Home() {
  return (
    <>
    <h1>Welcome to Your Friend Angel. A Friend that you never had..</h1>
    <p>Python API Status: {data.status}</p>
    <p>Python API Value: {data.value}</p>
    </>
  );
}
