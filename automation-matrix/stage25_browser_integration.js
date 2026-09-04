// echologic-voice-agent/automation-matrix/stage25_browser_integration.js
const express = require('express');
const http = require('http');

function initializeAutomationTokenServer() {
    console.log("=================================================================");
    console.log("MODULE: SERVER-SIDE VOICE SESSION TOKEN PROVISIONER");
    console.log("=================================================================");
    console.log("Enforcing single-use authorization parameters against Page 25...");

    const app = express();
    const port = process.env.PORT || 8080;

    // Automated Token Minting Routine mapping step 1 of reference guidelines
    app.get("/api/voice-token", async (req, res) => {
        const apiKey = process.env.ASSEMBLYAI_API_KEY;
        if (!apiKey) {
            console.log("Access Blocked: ASSEMBLYAI_API_KEY missing from system env variables.");
            return res.status(500).json({ error: "API Key not configured in environment parameters." });
        }

        console.log("Contacting ://assemblyai.com cloud to mint temporary token context...");
        try {
            const url = new URL("https://://assemblyai.com/v1/token");
            url.searchParams.set("expires_in_seconds", "300"); // 5-minute redemption window boundary
            url.searchParams.set("max_session_duration_seconds", "10800"); // 3-hour maximum ceiling cap

            const response = await fetch(url, {
                method: "GET",
                headers: { "Authorization": `Bearer ${apiKey}` }
            });

            if (!response.ok) {
                const errorLog = await response.text();
                return res.status(response.status).send(errorLog);
            }

            const data = await response.json();
            console.log(`Token secure minted: [...${data.token.slice(-12)}] (Single-Use context activated)`);
            res.json({ token: data.token });
        } catch (error) {
            res.status(500).send(error.message);
        }
    });

    const server = http.createServer(app);
    server.listen(port, () => {
        console.log(`\nAutomation token service engine running locally at http://localhost:${port}`);
        console.log(`Hit http://localhost:${port}/api/voice-token to fetch live authorization strings.`);
        console.log("-----------------------------------------------------------------");
        console.log("Press Ctrl+C to terminate this server loop and return to Matrix.");
    });
}

initializeAutomationTokenServer();
