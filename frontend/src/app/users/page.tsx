import Botton from "./botton";
export default async function UserPage() {
    const lat = process.env.TARGET_LAT;
    const lon = process.env.TARGET_LON;
    const apiKey = process.env.OPENWEATHER_API_KEY;

    let data: any = null;

    try {
        const weather = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}`, {
            cache: "no-store",
        });
        data = await weather.json();
        console.log(data);
    } catch {
      data = null;
    }
    return (
        <div>
            <div>Rain: {data?.weather?.[0]?.description}</div>
            <Botton />
        </div>
    );
}
