from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)


love_message = "Su mūsų mėnesio sukaktimi, Justyte! Nors esi toli, mano širdis visada su tavimi. Negaliu sulaukti, kada vėl susitiksime. Tu padarai kiekvieną dieną šviesesnę! Myliu tave labai labai❤️ Tikroji dovana tavęs laukia kai susitiksim ir bus prie kalėdinių. Bet čia geriausia, ką galėjau tau duoti šiandien. Kad ir kiek duočiau noriu tau duoti daugiau. Vis pasikartoju, bet pasikartoju, kad nepamirštum. Su kiekviena diena myliu vis labiau. Nesvarbu ar apsikvirčijam, ar gera nuotaika, ar bloga, bet be galo tave myliu ir noriu su tavimi eiti per visą gyvenimą. Noriu tave palaikyti, kad ir kas bebūtų. Myliu❤️❤️❤️"
countdown_date = "2024-12-26" 


html_template = """
<!DOCTYPE html>
<html lang="lt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Su Mūsų Sukaktimi!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background: linear-gradient(to bottom, #ffcccc, #ffe6e6);
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #ff0066;
            font-size: 2.5rem;
        }
        .message {
            margin-top: 20px;
            font-size: 1.5rem;
            background: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: inline-block;
        }
        .countdown {
            margin-top: 20px;
            font-size: 1.2rem;
            color: #ff0066;
        }
        .countdown p {
            font-size: 1rem;
            margin: 10px 0;
        }
        .music {
            margin-top: 30px;
            position: relative;
        }
        .record {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: url('/462574825_1867678456973260_1100714279920805442_n.jpg') no-repeat center/cover;
            margin: 0 auto;
            animation: spin 0s infinite linear;
        }
        .record.playing {
            animation: spin 3s infinite linear;
        }
        audio {
            margin-top: 20px;
            width: 80%;
        }
        .hearts {
            font-size: 2.5rem;
            margin: 20px 0;
            color: #ff0066;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
    <script>
        function updateCountdown(targetId, targetDate) {
            const targetElement = document.getElementById(targetId);
            const targetTime = new Date(targetDate).getTime();
            const now = new Date().getTime();
            const distance = targetTime - now;

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            targetElement.innerHTML =
                `${days} dienos, ${hours} valandos, ${minutes} minutės ir ${seconds} sekundės!`;

            if (distance < 0) {
                targetElement.innerHTML = "Mes jau kartu!";
            }
        }

        function toggleRecord() {
            const record = document.querySelector('.record');
            const audio = document.querySelector('audio');
            audio.addEventListener('play', () => record.classList.add('playing'));
            audio.addEventListener('pause', () => record.classList.remove('playing'));
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateCountdown('countdown', "{{ countdown_date }}");
            setInterval(() => updateCountdown('countdown', "{{ countdown_date }}"), 1000);
            toggleRecord();
        });
    </script>
</head>
<body>
    <h1>Ačiū už nuostabiausią gyvenimo mėnesį, Meile!</h1>
    <p class="message">{{ love_message }}</p>

    <div class="hearts">❤️❤️❤️</div>

    <div class="countdown">
        <h2>Iki mūsų susitikimo:</h2>
        <p id="countdown"></p>
    </div>

    <div class="music">
        <h2>Mūsų daina:</h2>
        <div class="record"></div>
        <audio controls>
            <source src="/yeah-yeah-yeahs-wait-they-don't-love-you-like-i-love-you-(maps)-made-with-Voicemod.mp3" type="audio/mpeg">
            Jūsų naršyklė nepalaiko garso elemento.
        </audio>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, love_message=love_message, countdown_date=countdown_date)

@app.route('/<path:filename>')
def audio(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
