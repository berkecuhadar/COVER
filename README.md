# C.O.V.E.R - Covert Operative Voice Exchange Room

**C.O.V.E.R** is a professional-grade social deduction Discord bot designed for voice channels and drawing activities. It operates on a simple yet engaging premise: everyone in the voice channel receives a secret word, except for one player—the **Covert Operative (Faker)**. Players must identify the imposter through discussion or drawing, while the Faker attempts to blend in without blowing their cover.

## Key Features
*   **Voice Integration:** Automatically fetches all members currently in a specific voice channel.
*   **Secret Assignments:** Delivers words and roles privately via Direct Messages (DMs).
*   **Multi-Server Support:** Handles active sessions across different Discord guilds simultaneously.
*   **Security Focused:** Uses environment variables to protect sensitive API tokens [2].

## Installation & Setup

### Prerequisites
*   Python 3.8 or higher.
*   A Discord Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications).

### Step-by-Step Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/berkecuhadar/COVER.git
    cd COVER
    ```

2.  **Install dependencies:**
    Using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration:**
    Create a `.env` file in the root directory. **Do not upload this file to GitHub** [2]. Add your bot token:
    ```text
    DISCORD_TOKEN=your_actual_bot_token_here
    ```

4.  **Database Setup:**
    Create a `data/` folder and a `data.json` file inside it. Use the following format:
    ```json
    [
      {"name": "Space Station"},
      {"name": "Submarine"}
    ]
    ```

5.  **Run the bot:**
    ```bash
    python cover.py
    ```

## How to Play

1.  Join a **Discord Voice Channel** with your friends.
2.  Type `!session` in a text channel.
3.  The bot will DM everyone their role. If you get a word, describe it carefully. If you are the **Faker**, try to guess the word from others' descriptions!
4.  Once the round is over, use `!endsession` to reveal the secret word and clear the session.

## Project Structure
*   `cover.py`: The core bot logic and command handlers.
*   `data/`: Directory containing the word database.
*   `.env.example`: Template for environment variables [2].
*   `requirements.txt`: List of required Python packages.

## License
This project is licensed under the MIT License.
