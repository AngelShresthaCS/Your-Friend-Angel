export async function GET() {
    const backendUrl = process.env.BACKEND_URL ?? "http://127.0.0.1:8000";

    try {
        const response = await fetch(`${backendUrl}/`, {
            cache: "no-store",
        });

        if (!response.ok) {
            return Response.json(
                { error: `Backend request failed with status ${response.status}` },
                { status: response.status },
            );
        }

        const data = await response.json();
        return Response.json(data);
    } catch {
        return Response.json(
            { error: "Unable to reach the backend service" },
            { status: 500 },
        );
    }
}