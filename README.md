# Swagan Voice TTS

AI-Powered Text-to-Speech web application powered by the Coqui TTS engine.

## Architecture

This project uses a split architecture for production deployment:

| Component | Technology | Deployment |
|-----------|-----------|------------|
| **TTS Backend** | Python + Flask + Coqui TTS | Railway (Docker) |
| **Web Frontend** | HTML/CSS/JS | Vercel |

## Project Structure

```
swagan-voice-tts/
├── server/
│   └── app.py              # Flask API server for TTS
├── frontend/
│   ├── index.html           # Web interface
│   └── vercel.json          # Vercel deployment config
├── Dockerfile               # Docker config for Railway
├── LICENSE
└── README.md
```

## Quick Start

### 1. Deploy Backend on Railway

1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. 2. Click **"New Project"** > **"Deploy from GitHub Repo"**
   3. 3. Select `vishnu-Swagan/swagan-voice-tts`
      4. 4. Railway will detect the `Dockerfile` and build automatically
         5. 5. Once deployed, copy your Railway URL (e.g., `https://swagan-voice-tts-production.up.railway.app`)
           
            6. ### 2. Deploy Frontend on Vercel
           
            7. 1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
               2. 2. Click **"Add New Project"** > Import `vishnu-Swagan/swagan-voice-tts`
                  3. 3. Set **Root Directory** to `frontend`
                     4. 4. Click **Deploy**
                        5. 5. Set your custom domain in Vercel dashboard
                          
                           6. ### 3. Connect Frontend to Backend
                          
                           7. 1. Open your Vercel-deployed frontend
                              2. 2. Paste your Railway backend URL in the "API Server URL" field
                                 3. 3. Type text and click "Synthesize Speech"
                                   
                                    4. ## API Endpoints
                                   
                                    5. | Method | Endpoint | Description |
                                    6. |--------|----------|-------------|
                                    7. | GET | `/` | API info and status |
                                    8. | GET | `/health` | Health check |
                                    9. | GET | `/api/tts?text=Hello` | Synthesize speech (returns WAV) |
                                    10. | POST | `/api/tts` | Synthesize speech (JSON body) |
                                    11. | GET | `/api/models` | List available TTS models |
                                   
                                    12. ## Local Development
                                   
                                    13. ### Run Backend Locally
                                   
                                    14. ```bash
                                        pip install TTS flask flask-cors
                                        cd server
                                        python app.py --port 5002
                                        ```

                                        ### Run with Docker

                                        ```bash
                                        docker build -t swagan-voice-tts .
                                        docker run -p 5002:5002 swagan-voice-tts
                                        ```

                                        Then open `frontend/index.html` in your browser and set API URL to `http://localhost:5002`.

                                        ## Environment Variables

                                        | Variable | Default | Description |
                                        |----------|---------|-------------|
                                        | `PORT` | `5002` | Server port |
                                        | `TTS_MODEL` | `tts_models/en/ljspeech/tacotron2-DDC` | TTS model to load |

                                        ## Built With

                                        - [Coqui TTS](https://github.com/coqui-ai/TTS) - Deep learning TTS engine
                                        - - [Flask](https://flask.palletsprojects.com/) - Python web framework
                                          - - [Railway](https://railway.app) - Backend hosting
                                            - - [Vercel](https://vercel.com) - Frontend hosting
                                             
                                              - ## License
                                             
                                              - This project is licensed under the Mozilla Public License 2.0 - see the [LICENSE](LICENSE) file for details.
                                             
                                              - ## Author
                                             
                                              - **Vishnu Swagan** - [GitHub](https://github.com/vishnu-Swagan)
