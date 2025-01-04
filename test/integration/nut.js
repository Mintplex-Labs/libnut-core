const { mouse, Point, screen, FileType, Region } = require("@mintplex-labs/nut-js");

async function moveMouse() {
    // Move the mouse in a sine wave pattern
    const amplitude = 100;
    const frequency = 0.05;
    for (let i = 0; i < 200; i++) {
        const x = i * 5;
        const y = amplitude * Math.sin(frequency * x) + 300;
        await mouse.move(new Point(x, y), 600);
    }

    // Take a screenshot
    screen.highlight(new Region(0, 0, await screen.width(), await screen.height()), "red");
    await screen.capture("screenshot.png", FileType.PNG);
    console.log("Screenshot taken!");
}
moveMouse();
