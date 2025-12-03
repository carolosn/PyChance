<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        const confettiLib = window.confetti;
    </script>
</head>

<body>
    <script>
    function confetti() {
        const duration = 1000;
        const end = Date.now() + duration;

        (function frame() {
            confettiLib({
                particleCount: 3,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });

            confettiLib({
                particleCount: 3,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
    }
    </script>
</body>
